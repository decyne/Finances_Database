import pickle

class SavedDictionary:


	# If the dictionary exists read in the file, otherwise create it
	def __init__(self,name):
		
		self.name = name
		try:
			with open (self.name,'rb') as fp:
				self.dict = pickle.load(fp)
		except:
			self.dict = {}
		
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	# Add an entry and save the dictionary
	def addEntry(self,entry,key):
		self.dict[key] = entry
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	# Remove the file and save the dictionary
	def removeEntry(self,key):
		del self.dict[key]
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	# Retrieve the dictionary in list format
	def getDict(self):
		return self.dict.items()

	# Retrieve the dictionary in list format
	def getEntry(self,key):
		return self.dict[key]
