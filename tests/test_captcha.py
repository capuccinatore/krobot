import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/../krobot/")

from captcha import CaptchaReader

class TestcaptchaReader:

	def test_read(self):
        
		capReader = CaptchaReader(os.path.dirname(__file__) + "/../krobot/Dico")
		captcha_str = capReader.read("tests/material/capt-test.png")

		assert captcha_str == "7Ks6W"
