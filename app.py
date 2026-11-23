from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_jobs():
    try:
        with open("jobs.json", "r") as f:
            return json.load(f)
    except:
        return [
            {"title": "Python Developer", "location": "Hyderabad", "skills": "Python, Flask"},
            {"title": "Frontend Developer", "location": "Hyderabad", "skills": "HTML, CSS, JS"},
            {"title": "AI Intern", "location": "Hyderabad", "skills": "Python, AI"}
        ]

def save_jobs(jobs):
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)

@app.route("/")
def home():
    jobs = load_jobs()
    search = request.args.get("search", "")
    if search:
        jobs = [j for j in jobs if search.lower() in j["skills"].lower()]
    return render_template("index.html", jobs=jobs, search=search)

@app.route("/add", methods=["POST"])
def add():
    jobs = load_jobs()
    new_job = {
        "title": request.form["title"],
        "location": request.form["location"],
        "skills": request.form["skills"]
    }
    jobs.append(new_job)
    save_jobs(jobs)
    return redirect("/")

@app.route("/delete/<int:num>")
def delete(num):
    jobs = load_jobs()
    jobs.pop(num)
    save_jobs(jobs)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)