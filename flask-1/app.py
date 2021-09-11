from flask import Flask, request, render_template, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal


app = Flask(__name__)

app.config["SECRET_KEY"] = "thisIsatestfO(())"


@app.route("/")
def landingpage():
    return render_template("index.html")


@app.route("/convert")
def convert_currency():
    c = CurrencyRates()
    currency_support = c.get_rates('USD')
    errors = False
    currency_list = ["USD"]

    currency_from_convert = request.args["convert-from"].upper()
    currency_to_convert = request.args["convert-to"].upper()
    amount_to_convert = request.args["amount"]

    for key in currency_support:
        currency_list.append(key)

    if currency_from_convert not in currency_list:
        errors = True
        flash("Not a valid code {}".format(currency_from_convert))

    if currency_to_convert not in currency_list:
        errors = True
        flash("Not a valid code {}".format(currency_to_convert))

    if not amount_to_convert:
        errors = True
        flash("Not a valid amount")

    if not errors:
        conversion_result = c.convert(
            currency_from_convert, currency_to_convert, Decimal(request.args["amount"]))

        currency_code = CurrencyCodes()
        currency_symbol = currency_code.get_symbol(currency_to_convert)

        converted_currency = "{:.2f}".format(conversion_result)
        return render_template("result.html", currency_symbol=currency_symbol, converted_currency=converted_currency)

    return render_template("index.html")
