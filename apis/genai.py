import os 
from google import genai
from google.genai import types

# Set environment variables
my_api_key = os.getenv('GENAI_KEY')
genai.api_key = my_api_key
# Create an genAI client using the key from our environment variable
client = genai.Client(
    api_key=my_api_key,
)

# Give results of rankings and scores for feedback
def feedback(resume, score, tier, job_title, job_description):
    # Specify the model to use and the messages to send
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction=
            f"You're a resume assistant helping the user understand why their resume was matched with the following job with a score of {score}% and tier: {tier}"
        ),
        contents= f"""
            Job Title: {job_title}
            Job Description:
            """
            {job_description}
            """
            Resume:
            """
            {resume}
            """
            """,
        #contents="What made the resume a good match or poor match?",
    )
    return response.text.strip()
