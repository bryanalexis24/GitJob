================================================================================
# GitJob 
##### "A smarter job discovery tool for software developers and engineers."
================================================================================



--------------------------------------------------------------------------------
Project Overview
--------------------------------------------------------------------------------
GitJob is a job discovery tool designed to help software developers and engineers
find job listings tailored specifically to their actual skills — not just vague
interests or titles. Unlike platforms like LinkedIn, GitJob focuses on aligning
your resume with real job descriptions to minimize wasted applications and 
maximize relevant matches.

--------------------------------------------------------------------------------
Purpose
--------------------------------------------------------------------------------
Too often, job seekers spend hours applying to roles that don’t align with their
experience or technical strengths. GitJob provides a smarter solution by ranking
jobs based on how well they match your resume — helping you focus on opportunities
where you're most likely to succeed.

--------------------------------------------------------------------------------
Primary Use Case
--------------------------------------------------------------------------------
- Unemployed individuals seeking software engineering opportunities
- College students searching for internships or new-grad SWE positions
- Anyone between jobs looking to pivot into a more relevant tech role

--------------------------------------------------------------------------------
Features
--------------------------------------------------------------------------------
- Filter job listings by keyword (e.g., "engineer", "python", "backend")
- Summarize job descriptions and display agency, location, and link
- Paste your resume directly into the terminal
- Score your resume against job descriptions using the TextRazor API
- Categorize job matches into 3 tiers based on keyword similarity:
    Tier 1: Strong match
    Tier 2: Moderate match
    Tier 3: Weak match

--------------------------------------------------------------------------------
Tech Stack
--------------------------------------------------------------------------------
Language:
- Python

APIs:
- USAJobs API (https://developer.usajobs.gov/)
- TextRazor API (https://www.textrazor.com/docs/python)

Modules:
- requests
- os
- textrazor

--------------------------------------------------------------------------------
Installation
--------------------------------------------------------------------------------
1. Clone the repository:
       git clone https://github.com/DaPillah/GitJob.git
       cd GitJob

2. Install dependencies:
       pip install -r requirements.txt

3. Set your API keys (replace with your actual keys):
       export USAJOB_AUTH_KEY="your_usajobs_api_key"
       export USAJOB_USER_AGENT="your_email@example.com"
       export TEXTRAZOR_KEY="your_textrazor_api_key"

4. Run the application:
       python main.py

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
Follow the terminal prompts to paste your resume and search job listings.
Jobs will be ranked by relevance based on resume content.

--------------------------------------------------------------------------------
Example Terminal Interaction
--------------------------------------------------------------------------------
Input:
    Enter resume text:
    "I am a backend engineer experienced in AWS, Python, and database design..."

Output:
    Top Matching Jobs:

    [Strong Match]
    Title: Backend Software Engineer
    Agency: Veterans Health Administration
    Location: San Diego, CA
    Score: 87%

    [Moderate Match]
    Title: Full Stack Developer
    Agency: Naval Sea Systems Command
    Location: Bremerton, WA
    Score: 62%

--------------------------------------------------------------------------------
Configuration
--------------------------------------------------------------------------------
Ensure the following environment variables are set before running:

    USAJOB_AUTH_KEY     - Your USAJobs API key
    USAJOB_USER_AGENT   - Your contact email for API registration
    TEXTRAZOR_KEY       - Your TextRazor API key

--------------------------------------------------------------------------------
Future Improvements
--------------------------------------------------------------------------------
- Support for uploading .pdf or .docx resume files
- Add a basic GUI using Flask or Tkinter
- Include job search history and bookmarking features



