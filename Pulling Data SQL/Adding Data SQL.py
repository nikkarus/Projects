import psycopg2
import sys
import pandas as pd
from sqlalchemy import create_engine
import os

path =  r'/Users/analytics/Desktop/Postgres setup/Data1 Short Pre Delimit.csv Delimited.csv'

engine = None

try:
    #engine = psycopg2.connect(database='NameplateDB', user='postgres', password='password', port='7777')
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:7777/NameplateDB',echo=False)
    connection = sql_engine.raw_connection()

    #'postgresql://' + os.environ['postgres'] + ':' +
        #os.environ['password'] + '@' + os.environ[
            #'localhost'] + ':' + os.environ['7777'] + '/' +
       # os.environ['NameplateDB'],
       # echo=False)

    df = pd.read_csv(path)
    df.to_sql(name='newtable', con=engine, if_exists = 'replace', index=False)


except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
finally:
    if engine:
        engine.close()


