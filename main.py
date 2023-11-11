import psycopg2

import psycopg2
cnx = psycopg2.connect(host='localhost', port='5432', database='Steam', user='postgres', password='teste123')
cursor = cnx.cursor()
cnx.autocommit = False

cursor.close()