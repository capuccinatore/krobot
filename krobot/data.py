import urllib2
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
        

