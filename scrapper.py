from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs

def get_jobs(key):
    indeed_jobs = get_indeed_jobs(key)
    so_jobs = get_so_jobs(key)
    jobs = indeed_jobs + so_jobs
    return jobs