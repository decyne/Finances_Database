# Open database/create files

from SavedDictionary import SavedDictionary
from prettytable import PrettyTable
import datetime

def categoryOpt():
	user_input = input("\
1) Add Category \n\
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
	user_input = input("\
1) Add Budget Category \n\
2) Remove Budget Category \n\
3) List BudgetCategories \n\
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

def summary():
    user_input = input("\
1) Daily Summary\n\
2) Weekly Summary\n\
3) Monthly Summary\n\
4) Yearly Summary\n\
5) Custom Summary\n\
\n\
0) Back")

    if(user_input == "1"):
        print("Daily Summary")
    elif(user_input == "5"):
        getUserDateRange()

def getUserDateRange():
    while 1:
        print("Please enter date in format YYYY-MM-DD")
        start_date = input("Enter beginning of timeperiod")
        end_date = input("enter end of timeperiod")
        try: 
            start_date = convertToDate(start_date)
            end_date = convertToDate(end_date)
        except:
            print("Incorrect date format, should be YYYY-MM-DD")
            continue

        if(not end_date > start_date):
            print("End date should be after start date")
            continue
        break
         
    return (start_date,end_date)   

def convertToDate(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

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
	user_input = input("\
1) Add Entry \n\
2) Get Summary \n\
3) Remove Entry \n\
4) Category Options \n\
5) Budget Options \n\
6) Import CSV \n\
\n\
0) Exit")

	if(user_input == "1"):
		print("Add entry")
	elif(user_input == "2"):
		summary()
	elif(user_input == "3"):
		print("Remove Entry")
	elif(user_input == "4"):
		categoryOpt()
	elif(user_input == "5"):
		budgetOpt()
	elif(user_input == "6"):
		print("import CSV")
	elif(input == "0"):
		exit

