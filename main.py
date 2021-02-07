from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from export import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    key = request.args.get("key")
    if key:
        key = key.lower()
        existingJobs = db.get(key)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(key)
            db[key] = jobs
    else:
        return redirect("/")
    return render_template("report.html", 
                           searchingBy = key, 
                           resultsNumber = len(jobs),
                           jobs = jobs)

@app.route("/export")
def export():
    try:
        key = request.args.get("key")
        if not key:
            raise Exception()
        key = key.lower()
        jobs = db.get(key)
        if not jobs:
            raise Exception()
        save_to_file(jobs, key)
        return send_file("jobs.csv")
    except:
        return redirect("/")
        

app.run(host="0.0.0.0")