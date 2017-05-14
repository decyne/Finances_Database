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
import csv
from prettytable import PrettyTable

class FinanceDatabase:

	MIN_DATE = '1753-1-1'
	MAX_DATE = '9999-12-31'

	# Creates a table with receipt index, date, description and purchase cost
	def __init__(self,table_name):
		
		#Probs should sanatise this. Won't make a difference in my current implementation but...
		self.table_name = table_name
		sqlite_file = self.table_name + '.sqlite'

		self.conn = 0
		self.c = 0

		self.conn = sqlite3.connect(self.sqlite_file)
		self.c =  self.conn.cursor()

		#Create table if it does not already exist
		try:
			c.execute('CREATE TABLE {tn} ({nf} {ft})'\
  		      .format(tn=self.table_name, nf='Receipt', ft='INTEGER'))

			c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    		    .format(tn=self.table_name, cn='Date', ct='date'))

			c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
   		     .format(tn=self.table_name, cn='Description', ct='TEXT'))

			c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    		    .format(tn=self.table_name, cn='Cost', ct='REAL'))

			c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    		    .format(tn=self.table_name, cn='Category', ct='TEXT'))
		except:
			print("Table already exists")
		
		self.conn.commit()
		self.conn.close()	

	# Connects to database
	def connect():
		self.conn = sqlite3.connect(self.sqlite_file)
		self.c =  self.conn.cursor()

	# Disconnects from database
	def disconnect():
		self.conn.commit()
		self.conn.close()	

	# Takes a csv file of the same format date,description,cost,category 
	# and adds it to the database 
	def importFromCSV(csv_name):
		connect()
		with open(csv_name,'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for row in csv_reader:
				rowAdd(row[0],row[1],row[2],row[3])

		disconnect()	
		return 0

	# Adds a row to the table from user input 
	def rowAdd(date,description,cost,category):
		connect()
		# Get largest index and increment to create unique index
		c.execute('SELECT MAX(receipt) FROM ' + self.table_name)
		id = c.fetchone()[0] + 1
		
		c.execute("INSERT INTO " + self.table_name + " VALUES (?,?,?,?,?)", (id,date,description,cost,category))

		disconnect()
		return 0

	# Removes a row from the table based on id 
	def rowRemove(id):
		connect()
		id = str(id)
		c.execute('DELETE FROM ' + self.table_name + ' WHERE Receipt=?', (id))

		disconnect()
		return 0

	# Returns the sum of the cost column for a specified inputs 
	def getCost(date_min,date_max,category):
		total = 0
		table = getSubTable(date_min,date_max,category)
		for row in table:
			total = total + row[3]
	
		return total 

	# Extracts part of the table depending on user input 
	def getSubTable(date_min,date_max,category):
		connect()
		if(category == "*"):
			c.execute('SELECT * FROM ' + self.table_name + ' WHERE date BETWEEN ? AND ?', (date_min,date_max))
		else:
			c.execute('SELECT * FROM ' + self.table_name + ' WHERE category=? AND date BETWEEN ? AND ?', (category,date_min,date_max))
		
		disconnect()
		return c.fetchall()

	# Prints part of the table 
	def printSubTable(sub_table):
		t = PrettyTable(['Reciept #','Date','Description','Cost($)','Category'])
		for row in sub_table:
			t.add_row(row)
		print(t)

	# Prints the whole table 
	def printTable():
		printSubTable(getSubTable(self.table_name,MIN_DATE,MAX_DATE,"*"))


db = FinanceDatabase("databasename")
#print(getCost(self.table_name,MIN_DATE,MAX_DATE,"U"))
#rowAdd(self.table_name,"2017-08-02","second",88,"U")
#print(getSubTable(self.table_name,MIN_DATE,MAX_DATE,"*"))
#importFromCSV(self.table_name,"example.csv")

