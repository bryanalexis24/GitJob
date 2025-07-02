import requests
import textrazor
import os

textrazor.api_key = os.environ.get('TEXTRAZOR_SECRET_API_ID')

user_input = input("Enter Your Resume: ")
client = textrazor.TextRazor(extractors=["entities", "topics"])

response = client.analyze(user_input)

print("\nEntities")
for entity in response.entities():
    print(f"- {entity.id} (Relevance: {entity.relevance_score} , Confidence: {entity.confidence_score})")

print("\nTopic")
for topic in response.topics():
    print(f"- {topic.label} (Score: {topic.score})")   

