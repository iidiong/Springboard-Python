from flask import Flask;

app = Flask(__name__);

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/<string>")
def welcome_home(string):
    return (f"welcome {string}")