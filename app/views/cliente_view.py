from flask import render_template

from app import app
from app.forms import client_form


@app.route("/hello")
def hello():
    return "Hello world !!! in Flask !!!"

@app.route("/hi", defaults={"visitor": None}, methods={"GET", "POST"})
@app.route("/hi/<string:visitor>")
def hi(visitor):
    return render_template("/clients/basic.html", name=visitor)

@app.route("/signup")
def signup():
    form = client_form.ClientForm()
    return render_template("/clients/form.html", form=form)
