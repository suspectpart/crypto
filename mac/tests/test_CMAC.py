from crypto.mac.CMAC import CMAC
from nose.tools import *

def test_cmac():
	message = b"Attack at dawn!"
	keys = (b"Sixteen Byte Key", b"Sixteen Bxxx Key", b"Sixteen Byte Kxx")
	cmac = CMAC(keys)
	eq_(cmac.verify(message, cmac.sign(message)), True)
	eq_(cmac.verify(message, b"Tag By Adversary"), False)