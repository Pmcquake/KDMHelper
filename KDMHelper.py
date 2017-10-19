import MySQLdb
import Tkinter
from Tkinter import *

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Connect to kdm database
db = MySQLdb.connect (host = "127.0.0.1",
						user = "root",
						passwd = "POOTS",
						db = "kdm")

# cursor object, allows execution of queries
cur = db.cursor()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Performs query on database, then displays the results
def getItem(query):
	cur.execute(query)
	items = ""
	for row in cur.fetchall():
		for col in row[1:]:
			items += str(col) + " | "
		items += "\n"
	textBox.delete(1.0, END)										# clear text box before writing new contents
	textBox.insert(INSERT, items)
	textBox.place(relheight = .80, relwidth = 1, rely = .15)


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Assembles query based on currently selected options, then sends it to getItem
def performQuery():
	select = "*"
	table = typeText.get()
	where = "affinities = '" + affinityText.get() + "'"	# this will get more complex as I add additional search options, might have implement a helper function

	query = "SELECT " + select + " FROM " + table
	if (affinityText.get() != "Any"):
		query += " WHERE " + where	
	getItem(query)

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Create Tkinter GUI
root = Tkinter.Tk()
root.title("KDMHelper")
root.geometry("1000x500")											# set window size
textBox = Text(root, width = 150)
textScroll = Scrollbar(textBox)

# OptionMenu implementation of type menu
typeText = StringVar(root)
typeText.set("Select Type")
typeButton = OptionMenu(root, typeText, "Weapons", "Armor", "Gear")

# Affinitiy menu
affinityText = StringVar(root)
affinityText.set("Select Affinity")
affinityButton = OptionMenu(root, affinityText, "Any", "UR", "RR", "DR", "LR", "UB", "RB", "DB", "LB", "UG", "RG", "DG", "LG")

# Search button
# Execute query when pressed
search = Tkinter.Button(root, text = "Search", command = performQuery)


# Actually open the GUI
typeButton.place(height = 25, relwidth = .12, relx = .05, rely = .1)
affinityButton.place(height = 25, relwidth = .12, relx = .23, rely = .1)
search.place(height = 25, relwidth = .1, relx = .45, rely = .05)
root.mainloop()


#---------------------------------------------------------------------------------------------------------------------------------------------#

# Cleanup
db.close()