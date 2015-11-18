import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/..")
import data
import datetime
import mock
import time

#def test_RU():
#    testUrlStr = "http://rbardenet.github.io/"
#    ru = data.RU("testRU", testUrlStr)
#    assert ru.url == testUrlStr
#    ru.fetchInformation()
#    assert ru.html[:3] == "<!D" 

def test_RU_fetchInfo() :

	filetest = "file://" + os.path.dirname(__file__)+"/material/test_data.html"
	
	def mytime(): return 1447000000#1447400000.0
	time.time = mytime
	#datetime.datetime.now = mock.Mock(return_value=datetime.datetime(2000, 11, 13))

	ru = data.RU("Barrois" , filetest)
	ru.fetchInfo()

	assert len(ru.menu) == 7
	assert ru.menu[0] == "Boeuf bourguignon"