jobs = [
    {"title": "Python Developer", "location": "Hyderabad", "skills": "Python, Flask"},
    {"title": "Frontend Developer", "location": "Bangalore", "skills": "HTML, CSS"},
    {"title": "AI Intern", "location": "Hyderabad", "skills": "Python, AI"}
]

def filter_jobs(jobs, skill):
    result = []
    for job in jobs:
        if skill.lower() in job["skills"].lower():
            result.append(job)
    return result

# Test it
print(filter_jobs(jobs, "Python"))
print(filter_jobs(jobs, "HTML"))
