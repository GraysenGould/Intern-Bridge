from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
import os
from openai import OpenAI
views = Blueprint("views", __name__)
from .format import format_response

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

    key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key = key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an interviewer for a Tech Company interviewing a candidate"},
            {
                "role": "assistant",
                "content": f"Before we start, here is a brief overview of the job: {job_description}"
            },
            {
                "role": "assistant", 
                "content": f"I see that your resume says: {resume_info}"
            },
            {
                "role": "system",
                "content": "Now ask the candidate 10 interview questions. Start with \'Its Great to meet you! Let's get this interview started\' "
            }
        ]
    )
    response = completion.choices[0].message.content

    new_response = format_response(response)
    #print(job_description, resume_info)

    return render_template("interview-questions.html",response = new_response)