
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
	if not os.path.isfile("/home/declan/Online_Repository/Finances_Database/finances_db.sqlite"):
		c.execute('CREATE TABLE {tn} ({nf} {ft})'\
		        .format(tn=table_name, nf='Receipt', ft='INTEGER'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
		        .format(tn=table_name, cn='Date', ct='TEXT'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
		        .format(tn=table_name, cn='Description', ct='TEXT'))

		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
		        .format(tn=table_name, cn='Cost', ct='REAL'))
	return 0

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

createTable("Finances 2017")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
