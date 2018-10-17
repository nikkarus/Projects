import psycopg2
import sys
import pandas as pd


con = None

try:
	con = psycopg2.connect(database='NameplateDB', user='postgres', password='password', port='7777')
	#cur = con.cursor()
	#dfout = pd.DataFrame(cur.execute('SELECT * FROM public."Nameplate_Data"'))
	dfout = pd.read_sql('SELECT * FROM public."Nameplate_Data"', con)
	print(dfout.head(5))
	dfout.to_csv('backup.csv', index=False)

except psycopg2.DatabaseError as e:
	print('Error %s' % e)
	sys.exit(1)
finally:
	if con:
		con.close()