import os,sys
from PIL import Image
import numpy
import urllib
import urllib2
from captcha import CaptchaReader
from bs4 import BeautifulSoup
from cookielib import CookieJar

website = "http://reservation.crous-lille.fr:82/index.php"
my_card = "856328"

class CreditFetcher(object):
	"""docstring for CreditFetcher"""

	def __init__(self):
		super(CreditFetcher, self).__init__()

	def fetch_credit(self, card_str):

		capReader = CaptchaReader("Dico")
		cap_str = ""
		
		# Creater headers, cookie manager and so on
		headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/537.86.2',
		}
		cj = CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

		# First request, open url
		response = opener.open('http://reservation.crous-lille.fr:82/index.php')

		cookie = response.headers.get('Set-Cookie')
		phpsesid = self.find_between(cookie, 0, ';')
		print phpsesid

		# Second request, ask for a sesion id
		req2 = urllib2.Request('http://reservation.crous-lille.fr:82/img.php')
		req2.add_header('cookie', cookie)
		f = opener.open(req2)
		text_req = f.read()
		print text_req

		# third request, ask for a captcha
		req3 = urllib2.Request('http://reservation.crous-lille.fr:82/' + text_req)
		img = opener.open(req3)
		
		with open('out.png', 'wb') as f:
			f.write(img.read())
		pil_image = Image.open('out.png')
		img = numpy.array(pil_image)

		# third request, ask for a captcha
		capReader = CaptchaReader("Dico")
		captcha_str = capReader.read("out.png")
		print captcha_str

		# fourth request, send captcha and card
		values = {'codecap' : captcha_str, 'codecl' : card_str}
		data = urllib.urlencode(values)
		req_4 = urllib2.Request('http://reservation.crous-lille.fr:82/recup.php', data)
		rep = opener.open(req_4)#urllib2.urlopen(req_4)
		info_results = rep.read()
		print info_results

		soup = BeautifulSoup(info_results, "html.parser")
		solde = soup.find_all('strong')
		money_left = self.find_between(str(solde[0]), 8, '<')

		print "You have " + money_left + "on your account, watch out!"
	
	def find_between(self, s, index_first, last ):
		try:
			start = index_first#s.index( first ) + len( first )
			end = s.index( last, start )
			return s[start:end]
		except ValueError:
			return ""


if __name__ == '__main__':
	ce = CreditFetcher()
	ce.fetch_credit(my_card)

