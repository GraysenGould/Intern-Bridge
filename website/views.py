from flask import Flask, Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")


@views.route("/interview",methods = ["GET", "POST"])
def interview():
    if request.method == "POST":
        print("Forms posted to backend")
    return render_template("interview.html")