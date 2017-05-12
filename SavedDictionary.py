import pickle

class SavedDictionary:

	def __init__(self,name):
		
		self.name = name
		try:
			with open (self.name,'rb') as fp:
				self.dict = pickle.load(fp)
		except:
			self.dict = {}
		
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	def addEntry(self,entry,key):
		self.dict[key] = entry
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	def removeEntry(self,icon):
		del self.dict[key]
		with open(self.name,'wb') as fp:
			pickle.dump(self.dict,fp)

	def getCategories(self):
		return self.dict.items()

d = SavedDictionary('test')
print(d.getCategories())

