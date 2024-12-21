#sample = "It's great to meet you! Let's get this interview started. Here are some questions to help us understand your skills and experiences better:\n\n1. Can you tell me about your background and how it has prepared you for this role in our company?\n2. What programming languages are you most comfortable with, and can you provide examples of projects where you've used them?\n3. Describe a challenging technical problem you've encountered in your previous work. How did you approach it, and what was the outcome?\n4. How do you prioritize your tasks when working on multiple projects or deadlines? Can you give an example?\n5. How do you stay current with new technologies and industry trends? Are there any recent innovations that you find particularly exciting?\n6. Can you walk us through a specific project where you worked as part of a team? What was your role, and how did you contribute to the team's success?\n7. How do you handle feedback or criticism of your work? Can you give an example of a time you incorporated feedback into your project?\n8. What methodologies (like Agile or Scrum) have you used in past projects, and how have they improved your workflow?\n9. Describe a time when you had to communicate a technical concept to a non-technical stakeholder. How did you ensure they understood?\n10. Finally, what excites you most about the possibility of working with our company, and what do you hope to achieve in this role?\n\nFeel free to take your time answering each question, and I look forward to hearing your insights!"

def format_response(response):
    lines = []
    prev = 0
    for i,c in enumerate(response):
        if c == "\n":
            lines.append(response[prev:i])
            prev = i + 1
    #print(lines)
    lines = [x for x in lines if x != ""] # get rid of empty elements
    new_response = {"greeting": lines[0], "questions": lines[1:]}
    return new_response


#print(format_response(sample))