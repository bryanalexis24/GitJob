from apis.resumeapi import getResume, calculateScore, tierList, extractKeywords, topFiveMatches
from apis.jobapi import fetch_jobs
from apis.genai import feedback

def main():
    resume_text = getResume().strip()
    if not resume_text:
        print("Resume can't be empty")
        return
    jobs = fetch_jobs("")
    if not jobs:
        print("No jobs found")
        return
    job_matches = topFiveMatches(resume_text, jobs)
    print("\nTop Matches:\n")
    for i in range(len(job_matches)):
        job = job_matches[i]
        print(f"{i+1}. {job['title']} @ {job['company']}")
        print(f"   Score: {job['score']}% | Tier: {job['tier']}")
        print(f"   Matched Skills: {', '.join(job['matched_skills'])}")
        print(f"   Link: {job['url']}")
        ai_feedback = feedback(
            resume_text,
            job["score"],
            job["tier"],
            job["title"],
            job["description"]
        )
        print("GenAI Feedback:")
        print("   " + ai_feedback.replace("\n", "\n   "))

if __name__ == "__main__":
    main()