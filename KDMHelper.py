import MySQLdb

# Connect to kdm database
db = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "POOTS",
						db = "kdm")

# cursor object, allows execution of queries
cur = db.cursor()

# example of executing a query
cur.execute("SELECT * FROM weapons")

# print everything returned by the query
for row in cur.fetchall():
	print row[1]

db.close()