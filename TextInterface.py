# Open database/create files

from SavedDictionary import SavedDictionary
from FinancesDatabase import FinanceDatabase
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
3) List Budget Categories \n\
\n\
0) Back")

	if(user_input == "1"):
		# Prompt until valid category is entered
		while 1:
			keylist = input("Enter list of category keys one after the other with no spaces ")
			try:
				for key in keylist:
					categories.getEntry(key)
				break
			except:
				print("Category key must exists in category list")
			
		name = str(input("Enter budget limit "))
		budget.addEntry(name,keylist)
	elif(user_input == "2"):
		key = input("Enter category key string to remove")
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
		(start_date,end_date) = getUserDateRange()
		showSummary(start_date,end_date)

# Prompts the user for a date range
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

def addEntry():

	# Prompt until a valid date is entered
	while 1:
		date = input("Enter date of purchase")
		try:
			convertToDate(date)
			break
		except:
			print("Incorrect date format, should be YYYY-MM-DD")
	description = input("Enter short description of purchase")
	cost = input("Enter cost of purchase")
	# Prompt until valid category is entered
	while 1:
		category = input("Enter category of purchase (Key form)")
		try:
			categories.getEntry(category)
			break		
		except:
			print("Category must exists in category list")
			
	expenses.rowAdd(date,description,cost,category)


def removeEntry():

	index = input("Enter reciept index of entry")
	expenses.rowRemove(index)

# Gets the amount spent vs amount budgeted for each budgeted category
def getBudgetSummary(start_date,end_date):

	# Very inneficient looping but screw it, should only be ~10 values max anyway	
	names = []
	for keys,cost in budget.getDict():
		expanded_keys = list(keys)
		name_list = []
		# Fetch name of each key from categories
		for individual_key in expanded_keys:
			name_list.append(categories.getEntry(individual_key))
		# Convert the list of categories to a single comma seperated string, add each comma seperated string to the list
		name_string = "+".join(name_list)
		names.append(name_string)	

	# Retrieves amount spent in each category for the time period
	cost_list = []
	for keys,cost in budget.getDict():
		expanded_keys = list(keys)
		cost = 0
	# Adds together the cost for each key listed for each budget item	
		for individual_key in expanded_keys:
			cost = cost + expenses.getCost(start_date,end_date,individual_key)
		cost_list.append(cost)
	
	budgeted = []
	for keys,cost in budget.getDict():
		budgeted.append(cost)

	summary = [names,cost_list,budgeted]
	summary = list(map(list, zip(*summary)))
	return summary

# Prints the list of items bought, income earnt and how much of each budget category is spent for the input time period
def showSummary(start_date,end_date):
	printSubTable(expenses.getSubTable(start_date,end_date,"*"),['Index','Date','Description','Cost','Key'])
	printSubTable(income.getSubTable(start_date,end_date,"*"),['Index','Date','Description','Cost','Key'])
	printSubTable(getBudgetSummary(start_date,end_date),['Categories','Expenditure','Budgeted'])

# Converts a string to a date object. Throws an error if the string is not in the valid format
def convertToDate(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

# Prints sub table, list_of_headers is list of strings where each string is a header of a column in the sub table 
def printSubTable(sub_table,list_of_headers):
	t = PrettyTable(list_of_headers)
	for row in sub_table:
		t.add_row(row)
	print(t)

def printExpenses():
	print("Expenses")
	printSubTable(expenses.getSubTable(FIRST_DATE,LAST_DATE,"*"),['Index','Date','Description','Cost','Key'])

def printIncome():
	print("Income")
	printSubTable(income.getSubTable(FIRST_DATE,LAST_DATE,"*"),['Index','Date','Description','Cost','Key'])

#------------------------------------------------------------------------------
# Object Setup
#------------------------------------------------------------------------------

categories = SavedDictionary("Categories")
budget = SavedDictionary("Budget")
expenses = FinanceDatabase("Expenses")
income = FinanceDatabase("Income") 

global FIRST_DATE
global LAST_DATE
FIRST_DATE = convertToDate("1990-01-01")
LAST_DATE = convertToDate("3000-12-31")

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
7) Print Expenses and Income \n\
\n\
0) Exit")

	if(user_input == "1"):
		addEntry()
	elif(user_input == "2"):
		summary()
	elif(user_input == "3"):
		removeEntry()
	elif(user_input == "4"):
		categoryOpt()
	elif(user_input == "5"):
		budgetOpt()
	elif(user_input == "6"):
		print("import CSV")
	elif(user_input == "7"):
		printExpenses()
		printIncome()
	elif(user_input == "0"):
		exit()
