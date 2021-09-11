from unittest import TestCase
from app import app


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_landingpage(self):
        with self.client:
            response = self.client.get("/")
            self.assertIn(b"<title>Currency Converter</title>", response.data)
            self.assertIn(b"Converting from", response.data)
            self.assertIn(b"Converting to", response.data)
            self.assertIn(b"Amount", response.data)
            self.assertEqual(200, response.status_code)

    def test_convert_from_usd_to_eur(self):
        with self.client:
            response = self.client.get(
                "/convert?convert-from=usd&convert-to=EUR&amount=100")
            self.assertEqual(200, response.status_code)
            self.assertIn(b"The result is", response.data)
            self.assertIn(b"Home", response.data)

    def test_empty_amount_field(self):
        with self.client:
            response = self.client.get(
                "/convert?convert-from=usd&convert-to=EUR&amount=")
            self.assertIn(b"Not a valid amount", response.data)
            self.assertEqual(200, response.status_code)

    def test_empty_convertingfrom_field(self):
        with self.client:
            response = self.client.get(
                "/convert?convert-from=&convert-to=EUR&amount=100")
            self.assertIn(b"Not a valid code ", response.data)
            self.assertEqual(200, response.status_code)

    def test_empty_convertingfrom_field(self):
        with self.client:
            response = self.client.get(
                "/convert?convert-from=usd&convert-to=&amount=100")
            self.assertIn(b"Not a valid code ", response.data)
            self.assertEqual(200, response.status_code)

    def test_invalid_currencysumbols(self):
        with self.client:
            response = self.client.get(
                "/convert?convert-from=yyy&convert-to=xxx&amount=")
            self.assertIn(b"Not a valid code YYY", response.data)
            self.assertIn(b"Not a valid code XXX", response.data)
            self.assertIn(b"Not a valid amount", response.data)
            self.assertEqual(200, response.status_code)
