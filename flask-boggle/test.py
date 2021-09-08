from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_homepage(self):
        with self.client:
            response = self.client.get("/")
            self.assertIn("board", session)
            self.assertIsNone(session.get("highscore"))
            self.assertIsNone(session.get("nplays"))
            self.assertIn(b"<p>High Score:", response.data)
            self.assertIn(b"Score:", response.data)
            self.assertIn(b"Seconds Left:", response.data)

    def test_valid_word(self):
        """Test valid dictionary word"""
        with self.client as client:
            with client.session_transaction() as sess:
                sess["board"] = [
                    ["S", "C", "H", "O", "O", "L"],
                    ["S", "C", "H", "O", "O", "L"],
                    ["S", "C", "H", "O", "O", "L"],
                    ["S", "C", "H", "O", "O", "L"],
                    ["S", "C", "H", "O", "O", "L"]]
            response = self.client.get("/check-word?word=school")
            print(response.json(["result"]))
            self.assertEqual(response.json["result"], "ok")

    def test_invalid_word(self):
        """Test valid dictionary word"""
        self.client.get("/")
        response = self.client.get("/check-word?word=chicken")
        self.assertEqual(response.json["result"], "not-on-board")

    def test_non_english_word(self):
        """Test non english word"""
        self.client.get("/")
        response = self.client.get("/check-word?word=abcdefg0")
        self.assertEqual(response.json["result"], "not-word")
