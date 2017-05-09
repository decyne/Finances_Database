#------------------------------------------------------------------------------
#	 2017_Database
#  
#  Description: Creates database used to track finances 
#               
#  Author: Declan Pratt
#
#  Date: April 2017 
#------------------------------------------------------------------------------

import sqlite3
import os.path
from prettytable import PrettyTable

MIN_DATE = '1753-1-1'
MAX_DATE = '9999-12-31'

#------------------------------------------------------------------------------
#	 Create Table
#  
#  Description: Creates a table with receipt index, date, description and 
#               purchase cost
#
#  Inputs: Table name
#------------------------------------------------------------------------------
def createTable(table_name):

	#Create table if it does not already exist
	try:
		c.execute('CREATE TABLE {tn} ({nf} {ft})'\
  	      .format(tn=table_name, nf='Receipt', ft='INTEGER'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    	    .format(tn=table_name, cn='Date', ct='date'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
   	     .format(tn=table_name, cn='Description', ct='TEXT'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    	    .format(tn=table_name, cn='Cost', ct='REAL'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    	    .format(tn=table_name, cn='Category', ct='TEXT'))
	except:
		print("Table already exists")

	return 0

#------------------------------------------------------------------------------
#	 Import from CSV
#  
#  Description: Takes a csv file and adds it to the database 
#
#  Inputs: N/A
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#	 Row Add
#  
#  Description: Adds a row to the table from user input 
#
#  Inputs: N/A
#------------------------------------------------------------------------------

def rowAdd(table_name,date,description,cost,category):

	# Get largest index and increment to create unique index
	c.execute('SELECT MAX(receipt) FROM ' + table_name)
	id = c.fetchone()[0] + 1
		
  # Should sanitise table name
	c.execute("INSERT INTO " + table_name + " VALUES (?,?,?,?,?)", (id,date,description,cost,category))

	return 0

#------------------------------------------------------------------------------
#	 Row Remove
#  
#  Description: Removes a row from the table based on id 
#
#  Inputs: N/A
#------------------------------------------------------------------------------

def rowRemove(table_name,id):
	id = str(id)
	c.execute('DELETE FROM ' + table_name + ' WHERE Receipt=?', (id))

	return 0

#------------------------------------------------------------------------------
#	 Get Cost
#  
#  Description: Returns the sum of the cost column for a specified inputs 
#
#  Inputs: Date range
#          Type
#------------------------------------------------------------------------------

def getCost(table,date_min,date_max,category):
	total = 0
	table = getSubTable(table,date_min,date_max,category)
	for row in table:
		total = total + row[3]
	
	return total 

#------------------------------------------------------------------------------
#	 Get Sub-Table
#  
#  Description: Extracts part of the table depending on user input 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

def getSubTable(table,date_min,date_max,category):
	c.execute('SELECT * FROM ' + table + ' WHERE category=? AND date BETWEEN ? AND ?', (category,date_min,date_max))
	return c.fetchall()

#------------------------------------------------------------------------------
#	 Print Sub-Table
#  
#  Description: Prints part of the table 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

def printSubTable(sub_table):
	t = PrettyTable(['Reciept #','Date','Description','Cost($)','Category'])
	for row in sub_table:
		t.add_row(row)
	print(t)

#------------------------------------------------------------------------------
#	 Print Table
#  
#  Description: Prints the whole table 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

def printTable(table_name):
	printSubTable(getSubTable(table_name,MIN_DATE,MAX_DATE,"U"))

#------------------------------------------------------------------------------
#	 Main
#  
#  Description: Runs the database program which asks for input 
#               
#  Inputs: N/A
#------------------------------------------------------------------------------

sqlite_file = 'finances_db.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table_name = "Finances_2017"

createTable(table_name)
#print(getCost(table_name,MIN_DATE,MAX_DATE,"U"))
#rowAdd(table_name,"2017-08-02","second",88,"U")
rowRemove(table_name,8)
printTable(table_name)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
