# Open database/create files

from SavedDictionary import SavedDictionary
from prettytable import PrettyTable

def categoryOpt():
	user_input = input("1) Add Category \n\
2) Remove Category \n\
3) List Categories \n\
\n\
0) Back")

	if(user_input == "1"):
		name = input("Enter category name ")
		key = input("Enter category key ")
		categories.addEntry(name,key)
	elif(user_input == "2"):
		key = input("Enter key of category to remove")
		categories.removeEntry(key)
	elif(user_input == "3"):
		printSubTable(categories.getDict(),['Category','Icon'])

	return 0

def budgetOpt():
	user_input = input("1) Add Budget Category \n\
2) Remove Budget Category \n\
3) List Budget Categories \n\
\n\
0) Back")

	if(user_input == "1"):
		key = input("Enter budget category name ")
		name = str(input("Enter budget limit "))
		budget.addEntry(name,key)
	elif(user_input == "2"):
		key = input("Enter name of category to remove")
		budget.removeEntry(key)
	elif(user_input == "3"):
		printSubTable(budget.getDict(),['Name','Budget'])

	return 0
	
# Prints table inout 
def printSubTable(sub_table,title_string):
	t = PrettyTable(title_string)
	for row in sub_table:
		t.add_row(row)
	print(t)

#------------------------------------------------------------------------------
# Object Setup
#------------------------------------------------------------------------------

categories = SavedDictionary("Categories")
budget = SavedDictionary("Budget")

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

while 1:
	user_input = input("1) Add Entry \n\
2) Get Summary \n\
3) Remove Entry \n\
4) Category Options \n\
5) Budget Options \n\
\n\
0) Exit")

	if(user_input == "1"):
		print("Add entry")
	elif(user_input == "2"):
		print("Get Summary")
	elif(user_input == "3"):
		print("Remove Entry")
	elif(user_input == "4"):
		categoryOpt()
	elif(user_input == "5"):
		budgetOpt()
	elif(input == "0"):
		exit

