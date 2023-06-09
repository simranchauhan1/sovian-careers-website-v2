from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db,add_job_to_db,see_applicants

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home1.html')

@app.route("/aspirant")
def hello_sovian():
  jobs = load_jobs_from_db()
  return render_template('aspirant.html', jobs=jobs)

@app.route("/recruiter")
def recruiter():
  return render_template('recruiter.html')  

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()

  return jsonify(jobs)


@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    
    return "Not Found", 404
  
  return render_template('jobpage.html', job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data,
                         job=job)

@app.route("/recruiter/add_job", methods=['post'])
def add_job():
  data= request.form
  add_job_to_db(data)
  return "inserted_successfully"     

@app.route("/add_jobs")
def add_jobs():
  return render_template('add_job.html')

@app.route("/see_applicants")  
def job_aspirants():
  application = see_applicants()
  print(application)
  return render_template('see_applicants.html', application=application)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
