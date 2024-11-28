from flask import Flask, Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def home():
    return render_template("base.html")