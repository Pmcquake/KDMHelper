import MySQLdb
import Tkinter
from Tkinter import *

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Connect to kdm database
db = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "POOTS",
						db = "kdm")

# cursor object, allows execution of queries
cur = db.cursor()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# display the return of a mySQLdb query using a Tkinter text box
def getItem():
	cur.execute("SELECT * FROM weapons")
	wep = ""
	text = Text(root, width = 100)
	for row in cur.fetchall():
		for col in row[1:]:
			wep += str(col) + " | "
	text.insert(INSERT, wep)
	text.pack()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Create Tkinter GUI
root = Tkinter.Tk()

# Button for testing out GUI
testButton = Tkinter.Button(root, text = "Test", command = getItem)


# Actually open the GUI
testButton.pack()
root.mainloop()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Cleanup
db.close()