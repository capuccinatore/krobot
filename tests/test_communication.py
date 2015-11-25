import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/../krobot")
import data
import datetime
#import mock
import time
import communication

def test_Communication():
    ruList = []
    personList = []
    comm = communication.Communication(personList, ruList)
    comm.startBot()
    comm.printMenus()
