from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssc/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs;"))

  result_dicts=[]
  for row in result._allrows():
   result_dicts.append(row._mapping)
  
  print(len(result_dicts))

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result._allrows():
      result_dicts.append(dict(row._mapping))
      return result_dicts
