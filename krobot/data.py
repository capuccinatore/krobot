import sys
import urllib2
import datetime
import locale
import time
from bs4 import BeautifulSoup

class Person(object):
    """
    gather daily prefences and constraints from a team member
    """

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.preferredRu = []
        self.timeSlot = [] # a list of 2 ints within which the person wants to eat, e.g. [1230,1345]

class RU(object):
	"""
	fetch and gather daily info on an given restaurant
	"""

	def __init__(self, name, url):
		super(RU, self).__init__()
		self.name = name
		self.url = url
		self.boolOpen = False
		self.menu = []

	def fetchInformation(self):
		with urllib.request.urlopen(self.url) as response:
			self.html = response.read().decode("iso-8859-1")
			marker = "menu_ru_plat\">"
			indexStart = self.html.find(marker)
			indexEnd = self.html.find("<", indexStart)
			self.menu.append(self.html[indexStart+len(marker):indexEnd])

	def fetchInfo(self):
		"""
		"""
		del self.menu[:]
		response = urllib2.urlopen(self.url)
		soup = BeautifulSoup(response.read(), "html.parser")
		days = soup.find_all('table', {"border" : "0", "cellpadding":"0", "cellspacing":"0", "width":"650"})

		current_day = datetime.datetime.now().day;
		targetting_string = "-1"
		for day in days:
			date = day.font.i.b.string
			list_info = date.split(" ")
			under_study_day = int(list_info[1])
			if under_study_day == current_day:
				targetting_string = day
				break

		if targetting_string == "-1":
			raise Exception("Week in " + self.name + "does not match with the current week. :(")

		# Here, targetting_string contains the html code containing the mode (among other things...)
		a = targetting_string.find_all("font", {"class":"menu_ru_plat"})

		self.menu = map(lambda item: unicode(item.string).encode('utf-8'), day.find_all("font", {"class":"menu_ru_plat"}))
		print self.menu
		

if __name__ == '__main__':

	def mytime(): return 1447000000#1447400000.0
	time.time = mytime

	ru = RU("Barrois" ,"http://www.crous-lille.fr/admin-site/restauration_menu_print_w.php?ru=26&midi=1&soir=1&nb_w=2")
	ru.fetchInfo()

