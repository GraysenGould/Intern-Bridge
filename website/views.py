from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
import os
from openai import OpenAI
views = Blueprint("views", __name__)
from .format import format_response
from .ai_response import AiResponse

#load chatchpt
ai_response = AiResponse()


@views.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")


@views.route("/interview",methods = ["GET", "POST"])
def interview():
    if request.method == "POST":
        session["jobDescriptionInput"] = request.form.get("jobDescriptionInput")
        session["resumeInput"] = request.form.get("resumeInput")
        return redirect(url_for("views.interview_questions"))
        #print("Forms posted to backend")
    return render_template("interview.html")


@views.route("/interview-questions",methods = ["GET", "POST"])
def interview_questions():

    job_description = session.get("jobDescriptionInput")
    resume_info = session.get("resumeInput")
    response = ai_response.generate_interview_questions(job_description, resume_info)

    return render_template("interview-questions.html",response = response)