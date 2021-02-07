import csv

def save_to_file(jobs, key):
  file = open("jobs.csv", mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow([f"keyword : {key}"])
  writer.writerow(["source", "title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return