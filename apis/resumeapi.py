import textrazor
import os

textrazor.api_key = os.environ.get('TEXTRAZOR_SECRET_API_ID')

# Need extracted job postings for comparison

"""
Prompts the user to pase their resume with multi line support
Returns the joined text
"""
def getResume():
    resume_text = ""
    while not resume_text.split():
        print("Enter Your Resume Below. Press ENTER Twice To Finish: \n")

        # Multi line support
        lines = []
        while True:
            line = input()
            if line.strip() == "": # Checks if user hits enter on an empty line so that it stops taking input
                break
            lines.append(line)

        resume_text = "\n".join(lines)
        if not resume_text:
            print("Please enter your resume\n")
    return user_input

"""
Analyzes the resume text and extracts relevant topics and skills using TextRazor
"""
def extractKeywords(text):
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    response = client.analyze(user_input)

    # Below needs to be changed. belongs to tier list function
    print("\nJob Titles")
    for topic in response.topics():
        print(f"- {topic.label} (Score: {round(topic.score * 100)}%)")   

    print("\nTier List:")

# Score calculator function using overlap from TextRazor

# Tier List function that asigns matches based on score

# Find top 5 matches