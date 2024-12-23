import os
from openai import OpenAI


class AiResponse ():
    def __init__ (self):
        self.key = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key = self.key)

    def generate_interview_questions (self,job_description, resume_info):
        completion = self.client.chat.completions.create(
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
        formated_response = self.format_response(response)
        return formated_response
    

    def format_response (self, response):
        lines = []
        prev = 0
        for i,c in enumerate(response):
            if c == "\n":
                lines.append(response[prev:i])
                prev = i + 1

        lines = [x for x in lines if x != ""] # get rid of empty elements
        new_response = {"greeting": lines[0], "questions": lines[1:]}
        return new_response
    
    def generate_answer_feedback (self, question, answer):
        completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpfull interview coach giving feedback. You asked the candidate the following mock interview question:"},
                    {
                        "role": "assistant",
                        "content": f"{question}"
                    },
                    {
                        "role": "user", 
                        "content": f"{answer}"
                    },
                    {
                        "role": "system",
                        "content": ("Give about 30 to 40 words of feedback on how the candidate answered the interview question. "
                                    "Give one thing good about the response and one thing that can be improved (reply in an objective tone). "
                                    "Remember, the response is being typed, so do not be as critical about lack of detail")
                    }
                ]
            )
        response = completion.choices[0].message.content
        return response
