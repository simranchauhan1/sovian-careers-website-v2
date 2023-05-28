from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

db_connection_string = os.getenv('DB_CONNECTION_STRING')

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
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id} ;"))
    rows = result._allrows()
  if len(rows) == 0:
    return None
  else:
    return rows[0]._mapping


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      f"""INSERT INTO applicaTions (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES({job_id}, "{data['full_name']}", "{data['email']}", "{data['linkedin_url']}", "{data['education']}", "{data['work_experience']}", "{data['resume_url']}")"""
    )
    conn.execute(query)
    conn.commit()