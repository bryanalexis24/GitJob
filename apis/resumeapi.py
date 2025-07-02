import requests
import textrazor
import os

my_api_key = os.getenv('TEXTRAZOR_KEY')
textrazor.api_key = my_api_key

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

# for entity in response.entities():
#     print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)
print(response)