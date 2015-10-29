from data import RU

class Caro(object):
	"""
	main caro class
	"""

	def __init__(self, medium):
		super(Caro, self).__init__()
		self.medium = medium

		ru_barois 	= RU("Barrois"  , "http://www.crous-lille.fr/admin-site/restauration_menu_print_w.php?ru=26&midi=1&soir=1&nb_w=2")
		ru_parisel  = RU("Pariselle", "http://www.crous-lille.fr/admin-site/restauration_menu_print_w.php?ru=19&midi=1&soir=1&nb_w=2")
		ru_sully 	= RU("Sully"    , "http://www.crous-lille.fr/admin-site/restauration_menu_print_w.php?ru=25&midi=1&soir=1&nb_w=2")

		self.listRu = [ru_barois, ru_parisel, ru_sully]

	def run(self):
		"""  
		clac clac clac
		"""

		
		
		pass

	def shutdown(self):
		""" 
		allow Caro to sleep
		"""
		pass
