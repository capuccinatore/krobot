#!/usr/bin/python

import sys
import urllib2
import datetime
import locale
from bs4 import BeautifulSoup

base_resto_url = 'http://www.crous-lille.fr/admin-site/restauration_menu_print_w.php?ru='
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

restos = [
	{'name':"Sully", 'id':"25"},	
	{'name':"Barois", 'id':"26"},	
	{'name':"Pariselle", 'id':"19"}	
]

text = "Bonjour,\n"

for resto in restos:
	resto_text = ""
	response = urllib2.urlopen(base_resto_url + resto['id'])
	soup = BeautifulSoup(response.read(), "html.parser")
	days = soup.find_all('table', {"border" : "0", "cellpadding":"0", "cellspacing":"0", "width":"650"})
	for day in days:
		date = day.font.i.b.string
		if date.replace(' ', '') == datetime.date.today().strftime('%A %e %B').replace(' ', ''):
			menu = map(lambda item: unicode(item.string), day.find_all("font", {"class":"menu_ru_plat"}))
			resto_text += "Au "+resto['name']+" aujourd'hui :\n\t-\t"
			resto_text += "\n\t-\t".join(menu)

	if(resto_text == ""):
		resto_text += "Au "+resto['name']+", rien aujourd'hui, peut etre ferme ?\n"
	text += resto_text+"\n"

print text
