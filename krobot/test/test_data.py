import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/..")
import data

#def test_RU():
#    testUrlStr = "http://rbardenet.github.io/"
#    ru = data.RU("testRU", testUrlStr)
#    assert ru.url == testUrlStr
#    ru.fetchInformation()
#    assert ru.html[:3] == "<!D" 

def test_RU_fetchInfo() :

	filetest = "file://" + os.path.dirname(__file__)+"/material/test_data.html"
	
	ru = data.RU("Barrois" , filetest)
	ru.fetchInfo()

	assert len(ru.menu) == 4
	assert ru.menu[1] == "Darne de saumon"