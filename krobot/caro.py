#import pause
import sys
import pause

import datetime
import xml.etree.ElementTree

from data import RU, Person
from credit import CreditFetcher
from mail import MailAgent

class Caro(object):
	"""
	main caro class
	"""

	def __init__(self, medium, mailAgent):
		super(Caro, self).__init__()
		self.medium = medium

		self.ruList = []
		self.usersList = []
		self.mailAgent = mailAgent

	def run(self):
		"""  
		clac clac clac
		"""	
		while True:

			self.extract_data()
			
			# fetch credit stuff
			self.fetch_credit()

			# fetch ru menu stuff
			#self.food_stuff()

			# Start talking with everybody
				# Todo

			# at time t : solve
				# Todo

			# Send result to everybody
				# Todo

			#TODO : pause until demain
			now =  datetime.date.today()
			pause.until(datetime.datetime(now.year, now.month, now.day+1, 10, 30))

	def extract_data(self):

		# Ru stuff
		try:
			ru_root = xml.etree.ElementTree.parse('ru.xml').getroot()
			str_http_adress = ru_root.find('adress').text
			
			for ru in ru_root.findall('ru'):
				ru_name = ru.find('name').text
				ru_id   = int(ru.find('id').text)

				self.ruList.append( RU(ru_name, str_http_adress.format(ru_id)))

		except Exception as e:
			print e
			raise ParseXmlException('error while parsing ru.xml')

		# User stuff
		try:
			user_root = xml.etree.ElementTree.parse('users.xml').getroot()
			str_http_adress = ru_root.find('adress').text
			
			for user in user_root.findall('user'):
				user_name = user.find('name').text
				user_id   = user.find('cardId').text
				user_mail = user.find('mail').text

				user_class = Person(user_name)
				user_class.cardId = user_id
				user_class.mail = user_mail

				self.usersList.append( user_class )

		except Exception as e:
			print e
			raise ParseXmlException('error while parsing users.xml')


	def fetch_credit(self):
		
		credFetch = CreditFetcher()

		for user in self.usersList:
			credit = credFetch.fetch_credit(user.cardId)
			user.creditLeft = credit;
			text = "Hi {0}!,\n You have {1} euros left on your card".format(user.name, credit)
			self.mailAgent.send(user.mail, 'CROUS', text)


	def food_stuff(self):
		for ru in self.ruList :
			ru.fetchInfo()

		#comm = Communication("some medium", self.ruList)

	def shutdown(self):
		""" 
		allow Caro to sleep
		"""
		pass


class ParseXmlException(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg

if __name__ == '__main__':

	if sys.argv[0] == "python":
		offset = 1
	elif sys.argv[0].startswith("caro.py"):
		offset = 0
	else:
		sys.exit("")

	mail = sys.argv[1 + offset]
	smtp = sys.argv[2 + offset]
	pseudo = sys.argv[3 + offset]
	mdp = sys.argv[4 + offset]
	mailAgent = MailAgent(mail, smtp, pseudo, mdp)

	c = Caro('skype', mailAgent)
	c.run()
