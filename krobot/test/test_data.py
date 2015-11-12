import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/..")
import data

def test_RU():
    testUrlStr = "http://rbardenet.github.io/"
    ru = data.RU("testRU", testUrlStr)
    assert ru.url == testUrlStr
    ru.fetchInformation()
    assert ru.html[:3] == "<!D" 


