import requests
import os

def fetch_jobs(keyword=""):
    token = os.getenv("FINDWORK_TOKEN")
    if not token:
        raise Exception("Missing token")
    headers = {"Authorization": f"Token {token}"}
    params = {"search": keyword}
    response = requests.get("https://findwork.dev/api/jobs/", headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch jobs: {response.status_code}")
    jobs = response.json().get("results", [])
    parsed_jobs = []
    for job in jobs:
        desc = job.get("description") or job.get("text") or job.get("summary") or ""
        if not desc.strip():
            continue
        parsed_jobs.append({
            "title": job.get("title") or job.get("role") or "Untitled Position",
            "company": job.get("company_name", "Unknown Company"),
            "url": job.get("url", ""),
            "description": desc
        })
    return parsed_jobs