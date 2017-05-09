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
#	 Row Add
#  
#  Description: Adds a row to the table from user input 
#
#  Inputs: N/A
#------------------------------------------------------------------------------

def rowAdd(table_name):
	print('Enter description')
	description = input()
	print('Enter date of purchase, or press enter for today\'s date')
	date = input()
	print('Enter cost')
	cost = input()
	print('Enter receipt index')
	receipt = input()
	print('Enter Category')
	category = input()

  # Should sanitise table name
	c.execute("INSERT INTO " + table_name + " VALUES (?,?,?,?,?)", (receipt,date,description,cost,category))

	return 0

#------------------------------------------------------------------------------
#	 Import from CSV
#  
#  Description: Takes a csv file and adds it to the database 
#
#  Inputs: N/A
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#	 Return Total
#  
#  Description: Returns the sum of the cost column for a specified inputs 
#
#  Inputs: Date range
#          Type
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#	 User Return Prompt
#  
#  Description: Asks the user for a range and returns the total cost of all items in that range 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#	 User Text Interface
#  
#  Description: Provides a user interface for the user 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#	 Get User Selection
#  
#  Description: Gets a range of values to select from the table using user input 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

#def getTableRange():

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
	printSubTable(getSubTable(table_name,MIN_DATE,MAX_DATE,"P"))


#------------------------------------------------------------------------------
#	 Print User Selection
#  
#  Description: Prints the whole table 
#
#  Inputs: N/A 
#------------------------------------------------------------------------------

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
#rowAdd(table_name)
printTable(table_name)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
