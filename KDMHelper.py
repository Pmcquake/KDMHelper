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
def getItem(select, table, where, textBox):
	query = "SELECT " + select + " FROM " + table
	if (where == None):												# if there is no WHERE statement
		cur.execute(query)
		items = ""
		for row in cur.fetchall():
			for col in row[1:]:
				items += str(col) + " | "
			items += "\n"
		textBox.delete(1.0, END)									# clear text box before writing new contents
		textBox.insert(INSERT, items)
		textBox.pack()
	else:															# if there is a WHERE statement
		query += " WHERE " + where
		getWhere(query, textBox)


# takes care of queries when there is a WHERE statement
def getWhere(query, textBox):
	cur.execute(query)
	items = ""
	for row in cur.fetchall():
		for col in row[1:]:
			items += str(col) + " | "
		items += "\n"
	textBox.delete(1.0, END)										# clear text box before writing new contents
	textBox.insert(INSERT, items)
	textBox.pack()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Create Tkinter GUI
root = Tkinter.Tk()
textBox = Text(root, width = 150)

# Button for testing out GUI
weaponTest = Tkinter.Button(root, text = "Weapons", command = lambda: getItem("*", "weapons", None, textBox))
oneWeapon = Tkinter.Button(root, text = "One Weapon", command = lambda: getItem("*", "weapons", "id = 1", textBox))
armorTest = Tkinter.Button(root, text = "Armor", command = lambda: getItem("*", "armor", None, textBox))
gearTest = Tkinter.Button(root, text = "Gear", command = lambda: getItem("*", "gear", None, textBox))

# Actually open the GUI
weaponTest.pack()
oneWeapon.pack()
armorTest.pack()
gearTest.pack()
root.mainloop()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Cleanup
db.close()