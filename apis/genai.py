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

# Specify the model to use and the messages to send
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
      system_instruction="Give constructive feedback on the results of the resume to job match based on the score/tier. If in tier 1, highlight what skills gave the user a high rating. If in other two, tell user which keywords are missing"
    ),
    contents="What made the resume a good match or poor match?",
)

print(response.text)

"""
Give results of rankings and scores for feedback
"""