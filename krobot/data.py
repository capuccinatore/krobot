import urllib.request
import re

class RU():
    """
    gather daily info on an given restaurant
    """

    def __init__(self, name, url):
        super(RU, self).__init__()
        self.name = name
        self.url = url

    def fetchInformation(self):
        with urllib.request.urlopen(self.url) as response:
            html = response.read()
            #index = html.find("menu_ru_plat>")
            print("menu" in html)

