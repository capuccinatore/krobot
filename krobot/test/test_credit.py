import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__)+"/..")

from credit import CaptchaReader

class TestcaptchaReader:

    def test_read(self):
        
        capReader = CaptchaReader("Dico")
        captcha_str = capReader.read("test/material/capt-test.png")

        assert captcha_str == "7Ks6W"
