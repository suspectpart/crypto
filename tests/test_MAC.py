from nose.tools import *
from crypto.MAC import *

def test_cbc_mac_sign_and_verify():
	key1 = b'0011223344556677'
	key2 = b'FFXXAABBCCDDEEFF'
	message = b'A message spanning multiple blocks for which we want to generate a tag'
	cbc_mac = CBC_MAC(key1, key2)

	assert cbc_mac.sign(b"S dasdas das dddd dcascqwA") != cbc_mac.sign(b"Message B adxxxxaqwd dasdasdas")
	eq_(cbc_mac.verify(message, cbc_mac.sign(message)), True) 
	eq_(cbc_mac.verify(message, b"Tag by adversary"), False) 
	eq_(cbc_mac.verify(b"Message by adversary", cbc_mac.sign(message)), False)

def test_cmac():
	message = b"Attack at dawn!"
	keys = (b"Sixteen Byte Key", b"Sixteen Bxxx Key", b"Sixteen Byte Kxx")
	cmac = CMAC(keys)
	eq_(cmac.verify(message, cmac.sign(message)), True)
	eq_(cmac.verify(message, b"Tag By Adversary"), False)

def test_one_time_mac():
	message = b"Attack at dawn!"
	one_time_mac = One_Time_Mac()
	key = one_time_mac.new_key()
	tag = one_time_mac.sign(message, key)
	ok_(one_time_mac.verify(message, key, tag))
	eq_(one_time_mac.sign("\x01\x01", (1,1)), (1 ** 3 + 1 * 1 ** 1 + 1) + 1 % 1000)   

def test_pad():
	eq_(pad(b'\xFF\xFF\xFF\xFF', 4), b'\xFF\xFF\xFF\xFF\x80\x00\x00\x00')
	eq_(pad(b'\xFF\xFF\xFF', 4), b'\xFF\xFF\xFF\x80')
	eq_(pad(b'\xFF\xFF', 4), b'\xFF\xFF\x80\x00')