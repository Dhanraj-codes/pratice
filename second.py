import json

# Step 2: Load saved jobs, or use default if first time
try:
    with open("jobs.json", "r") as f:
        jobs = json.load(f)
except:
    jobs = [
        {"title": "Python Developer", "location": "Hyderabad", "skills": "Python, Flask"},
        {"title": "Frontend Developer", "location": "Hyderabad", "skills": "HTML, CSS, JS"},
        {"title": "AI Intern", "location": "Hyderabad", "skills": "Python, AI"}
    ]

def filter_jobs(jobs, skill):
    result = []
    for job in jobs:
        if skill.lower() in job["skills"].lower():
            result.append(job)
    return result

def save_jobs():
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)
    print("jobs saved!")

while True:
    print("\n--- JOB PORTAL ---")
    print("1. Search Job by Skill")
    print("2. Add New Job")
    print("3. Show All Jobs")
    print("4. Delete a Job")
    print("5. Update a Job")
    print("6. Exit")
    choice = input("enter your choice (1/2/3/4/5/6): ")

    if choice == "6":
        print("bye bye, happy job hunting!")
        break

    if choice == "1":
        skill = input("enter skill to search: ")
        result = filter_jobs(jobs, skill)
        if len(result) == 0:
            print("no jobs")
        else:
            for job in result:
                print(job["title"], "-", job["location"], "-", job["skills"])

    if choice == "2":
        title = input("enter job title: ")
        location = input("enter location: ")
        skills = input("enter skills (like python,css): ")
        new_job = {"title": title, "location": location, "skills": skills}
        jobs.append(new_job)
        save_jobs()
        print("job added successfully!")

    if choice == "3":
        print("\n--- ALL JOBS ---")
        if len(jobs) == 0:
            print("no jobs yet")
        else:
            for job in jobs:
                print(job["title"], "-", job["location"], "-", job["skills"])

    if choice == "4":
        print("\n--- DELETE JOB ---")
        for i in range(len(jobs)):
            print(i, "-", jobs[i]["title"], "-", jobs[i]["location"])
        num = int(input("enter job number to delete: "))
        deleted = jobs.pop(num)
        save_jobs()
        print("deleted:", deleted["title"])

    if choice == "5":
        print("\n--- UPDATE JOB ---")
        for i in range(len(jobs)):
            print(i, "-", jobs[i]["title"], "-", jobs[i]["location"], "-", jobs[i]["skills"])
        num = int(input("enter job number to update: "))
        print("leave blank if you don't want to change")
        new_title = input("new title: ")
        if new_title != "":
            jobs[num]["title"] = new_title
        new_location = input("new location: ")
        if new_location != "":
            jobs[num]["location"] = new_location
        new_skills = input("new skills: ")
        if new_skills != "":
            jobs[num]["skills"] = new_skills
        save_jobs()
        print("job updated successfully!")