from flask import render_template
from typing import Any
from . import create_app
from .api import dices


app = create_app()

@app.errorhandler(404)
def handle_not_found(error):
    return render_template(
        "errors/error.html",
        error_name = "Not found",
        error_message = error.args,
        status_code = 404
    ), 404


def wrap_template_rendering(template_name: str, **context: Any):
    return render_template(template_name, _author="Jonny", **context)

@app.route("/")
def home():
    return wrap_template_rendering("home.html")

@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_world(name: str = None):
    return wrap_template_rendering("hello.html", _name=name)

@app.route("/dices")
def handle_dices():
    return wrap_template_rendering("dice.html", _dices=dices)

