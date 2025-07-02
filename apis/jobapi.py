import requests
import os


def get_headers():
    auth_key = os.environ.get('USAJOB_AUTH_KEY')
    user_agent = os.environ.get('USAJOB_USER_AGENT')

    if not auth_key or not auth_key:
        raise ValueError("missing auth-key or user-agent")

    return{
        "User-Agent": user_agent,
        "Authorization-Key": auth_key
    }
    

def build_params(keyword="engineer", job_abundance=1):
    return {
    "Keyword": keyword,
    "ResultsPerPage": job_abundance
    }

def fetch_jobs(headers, params):
    url = "https://data.usajobs.gov/api/search"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception("failed to fetch data {response.status_code}")
    return response.json()

def parse_jobs(data):
        results = []
        for job in data.get("SearchResult", {}).get("SearchResultItems", []):
          descriptor = job['MatchedObjectDescriptor']
          results.append({"title": descriptor.get('PositionTitle'),
          "agency": descriptor.get('OrganizationName'),
          "location": descriptor.get('PositionLocationDisplay'),
          "url": descriptor.get('PositionURI'),
          "summary": descriptor.get('UserArea', {}).get('Details', {}).get('JobSummary')
          })
        return results


def print_jobs(jobs):
    for job in jobs:
        print(f"Title: {job['title']}")
        print(f"Agency: {job['agency']}")
        print(f"Location: {job['location']}")
        print(f"URL: {job['url']}")
        print(f"Summary: {job['summary']}")