# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def do_add():
    """ Do addition operation using parameter a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(add(a, b))
    return result


@app.route("/sub")
def do_sub():
    """ Do subtraction operation using parameter a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(sub(a, b))
    return result


@app.route("/div")
def do_div():
    """ Do division operation using parameter a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(div(a, b))
    return result


@app.route("/mult")
def do_mult():
    """ Do multiplication operation using parameter a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(mult(a, b))
    return result


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math calculations on a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
