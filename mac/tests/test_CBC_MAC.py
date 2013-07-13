from crypto.mac.CBC_MAC import CBC_MAC
from nose.tools import *

def test_cbc_mac_sign_and_verify():
	key1 = b'0011223344556677'
	key2 = b'FFXXAABBCCDDEEFF'
	message = b'A message spanning multiple blocks for which we want to generate a tag'
	cbc_mac = CBC_MAC((key1, key2))

	assert cbc_mac.sign(b"S dasdas das dddd dcascqwA") != cbc_mac.sign(b"Message B adxxxxaqwd dasdasdas")
	eq_(cbc_mac.verify(message, cbc_mac.sign(message)), True) 
	eq_(cbc_mac.verify(message, b"Tag by adversary"), False) 
	eq_(cbc_mac.verify(b"Message by adversary", cbc_mac.sign(message)), False)