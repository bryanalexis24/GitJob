import textrazor
import os

textrazor.api_key = os.environ.get('TEXTRAZOR_SECRET_API_ID')

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
            # Checks if user hits enter on an empty line so that it stops taking input
            if line.strip() == "":
                break
            lines.append(line)
        resume_text = "\n".join(lines)
        if not resume_text:
            print("Please enter your resume\n")
    return resume_text

"""
Analyzes the resume text and extracts relevant topics and skills using TextRazor
"""
def extractKeywords(text):
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    response = client.analyze(text)
    keywords = set()
    for entity in response.entities():
        if entity.id and entity.confidence_score >= 0.5:
            keywords.add(entity.id.lower())
    return keywords

"""
Calculates score using overlap from TextRazor
Takes two arguments, the extracted keywords and the job desc skills
"""
def calculateScore(resume_keywords, job_keywords):
    if not resume_keywords or not job_keywords:
        return 0, []
    overlap = resume_keywords & job_keywords
    score = len(overlap) / len(job_keywords) * 100
    return round(score, 2), list(overlap)

"""
Assigns matches in tier list rankings based on score
"""
def tierList(score):
    if score >= 95:
        return "👑 Tier 1 (Excellent Match)"
    elif score >= 90 and score < 95:
        return "🤷🏽 Tier 2 (Strong Match)"
    else:
        return "🤨 Tier 3 (Weak Match)"

"""
Finds the top 5 matches for resume
"""
def topFiveMatches(resume_text, jobs):
    resume_keywords = extractKeywords(resume_text) 
    print("Resume Keywords:", resume_keywords)
    job_matches = []
    for job in jobs[:10]:
        job_desc = job["summary"]
        job_keywords = extractKeywords(job_desc)
        print("Job Keywords:", job_keywords)
        score, matched = calculateScore(resume_keywords, job_keywords)
        job_matches.append({
            "title": job["title"],
            "company": job["company"],
            "url": job["url"],
            "description": job_desc,
            "score": score,
            "tier": tierList(score),
            "matched_skills": matched
        })
    job_matches.sort(key=lambda job: job["score"], reverse=True)
    top_matches = job_matches[:5]
    return top_matches









    