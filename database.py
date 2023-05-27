from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
my_secret = os.environ['DB_CONNECTION_STRING']
print(db_connection_string)

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssc/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
  for row in result._allrows():
    result_dicts.append(dict(row._mapping))

  return result_dicts


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),       val=id)
    rows = result._allrows()
  if len(rows) == 0:
    return None
  else:
    return rows[0]._mapping


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, email, linkedin_url, education, work_experience, resume_url)"
    )
  conn.execute(query,
              job_id=job_id,
              full_name=data['full_name'],
              email=data['email'],
              linkedin_url=data['linkedin_url'],
              education=data['education'],
              work_experience=data['work_experience'],
              resume_url=data['resume_url'])
