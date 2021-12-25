import unittest

from app import app
from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = True

app.config["Testing"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

db.drop_all()
db.create_all()


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        User.query.delete()

        user = User(first_name="Henry", last_name="Paul",
                    image_url="http//thisistest.com")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_list_users_data(self):
        with app.test_client() as client:
            resp = client.get("/users")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("Henry" in resp.get_data(as_text=True))
            
    def test_add_new_users_form(self):
        with app.test_client() as client:
            resp = client.get("/users/new")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("Create a user" in resp.get_data(as_text=True))

    def test_list_users_redirect(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 302)

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            self.assertEqual(resp.status_code, 200)

    def test_new_user_with_no_post(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            self.assertEqual(resp.status_code, 302)

    def test_show_invalid_user(self):
        with app.test_client() as client:
            resp = client.get("/users/100")
            self.assertEqual(resp.status_code, 302)
    
    def test_delete_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}/delete")
            self.assertEqual(resp.status_code, 302)
            self.assertTrue("Users", resp.get_data(as_text=True))



