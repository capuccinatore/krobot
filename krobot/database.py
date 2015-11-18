class DataBase(object):
	"""
	docstring for DataBase
	"""

	def __init__(self):
		super(DataBase, self).__init__()

		self.constraint = []
		self.listRu 	= []

	def addConstraint(self, constraint):
		pass

	def removeAll(self):
		del self.constraint[:]
		del self.listRu[:]

	
