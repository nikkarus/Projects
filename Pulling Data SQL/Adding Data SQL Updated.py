from sqlalchemy import create_engine
import psycopg2
import io
import pandas as pd


path =  r'/Users/analytics/Desktop/Postgres setup/Data1 Short Pre Delimit.csv Delimited.csv' #delegates path to csv
df = pd.read_csv(path) #converts csv to pandas df
engine = create_engine('postgresql+psycopg2://postgres:password@localhost:7777/NameplateDB', echo=False) #creates path to connection of Postgres

df.head(0).to_sql('table_set', engine,if_exists='append',index=False) #truncates the table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'table_set', null="") # null values become ''
conn.commit()

