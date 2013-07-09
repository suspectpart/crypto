from nose.tools import *
from crypto.MAC import CBC_MAC

def test_cbc_mac():
	key1 = b'0011223344556677'
	key2 = b'FFXXAABBCCDDEEFF'
	message = b'A message spanning multiple blocks for which we want to generate a tag'
	cbc_mac = CBC_MAC(key1, key2)

	assert cbc_mac.generate_tag(b"S dasdas das dddd dcascqwA") != cbc_mac.generate_tag(b"Message B adxxxxaqwd dasdasdas")
	eq_(cbc_mac.verify_tag(message, cbc_mac.generate_tag(message)), True) 
	eq_(cbc_mac.verify_tag(message, b"Tag by adversary"), False) 
	eq_(cbc_mac.verify_tag(b"Message by adversary", cbc_mac.generate_tag(message)), False)