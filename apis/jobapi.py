import requests
import os


def get_headers():
    auth_key = os.environ.get('USAJOB_AUTH_KEY')
    user_agent = os.environ.get('USAJOB_USER_AGENT')

    if not auth_key:
        raise ValueError("missing auth-key")
    elif not user_agent:
        raise ValueError("missing user-agent")

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
        raise Exception(f"failed to fetch data {response.status_code}")
    data = response.json()
    return parse_jobs(data)

def parse_jobs(data):
        results = []
        for job in data.get("SearchResult", {}).get("SearchResultItems", []):
          descriptor = job['MatchedObjectDescriptor']
          results.append({"title": descriptor.get('PositionTitle'),
          "company": descriptor.get('OrganizationName'),
          "location": descriptor.get('PositionLocationDisplay'),
          "url": descriptor.get('PositionURI'),
          "summary": descriptor.get('UserArea', {}).get('Details', {}).get('JobSummary')
          })
        return results

