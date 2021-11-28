from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = True

app.config["Testing"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        user = User(first_name="Henry", last_name="Paul",
                    image_url="http//thisistest.com")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_list_users_redirect(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 302)

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            self.assertEqual(resp.status_code, 200)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            self.assertEqual(resp.status_code, 200)

    def test_show_invalid_user(self):
        with app.test_client() as client:
            resp = client.get("/users/100")
            self.assertEqual(resp.status_code, 404)
