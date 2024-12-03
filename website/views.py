from flask import Flask, Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")


@views.route("/interview",methods = ["GET", "POST"])
def interview():
    if request.method == "POST":
        print(request.form.get("jobDescriptionInput"))
        return redirect(url_for("views.interview_questions"))
        #print("Forms posted to backend")
    return render_template("interview.html")


@views.route("/interview-questions",methods = ["GET", "POST"])
def interview_questions():
    return render_template("interview-questions.html")