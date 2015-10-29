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
        self.boolOpen = 0
        self.menu = []

    def fetchInformation(self):
        with urllib.request.urlopen(self.url) as response:
            self.html = response.read().decode("iso-8859-1")
            marker = "menu_ru_plat\">"
            indexStart = self.html.find(marker)
            indexEnd = self.html.find("<", indexStart)
            self.menu.append(self.html[indexStart+len(marker):indexEnd])


