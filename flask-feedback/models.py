from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """ Connect to Database """
    db.app = app
    db.init_app(app)


class User(db.Model):
    """ Create a user model """

    __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(20), unique=True,
                         primary_key=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    feedback = db.relationship(
        "Feedback", backref="users", cascade="all,delete")

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """ Register user with hashed password and return user."""
        hashed = bcrypt.generate_password_hash(password)

        # turn bytestring in to normal (unicode utf) string
        hashed_utf8 = hashed.decode('utf8')

        # return instance of user with username and hashed password
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists and password is correct
        Return user if valid; else return falsey
        """
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False


class Feedback(db.Model):
    """ Create a Feedback model """

    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey(
        'users.username'), nullable=False)
