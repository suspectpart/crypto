from nose.tools import *
from crypto.utils import *


def test_mac_pad():
	eq_(mac_pad(b'\xFF\xFF\xFF\xFF', 4), b'\xFF\xFF\xFF\xFF\x80\x00\x00\x00')
	eq_(mac_pad(b'\xFF\xFF\xFF', 4), b'\xFF\xFF\xFF\x80')
	eq_(mac_pad(b'\xFF\xFF', 4), b'\xFF\xFF\x80\x00')

def test_pad():
	eq_(pad(b'Attack at dawn', 16), b'Attack at dawn\x02\x02')
	eq_(pad(b'1234567890', 16), b'1234567890\x06\x06\x06\x06\x06\x06')
	eq_(pad(b'Attack on monday', 16), b'Attack on monday\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10')

def test_unpad():
	eq_(unpad(b'Attack at dawn\x02\x02'), b'Attack at dawn')
	eq_(unpad(b'1234567890\x06\x06\x06\x06\x06\x06'), b'1234567890')
	eq_(unpad(b'Attack on monday\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'), b'Attack on monday') 

def test_xor():
	x = b'\x00\xFF'
	y = b'\xFF\x00'
	eq_(xor(x,y), b'\xFF\xFF')

def test_get_blocks():
	text = b"Sixteen Byte MsgSixteen Byte Msg" # 32 bytes = exactly two blocks
	blocks = get_blocks(text, 16)
	eq_(len(blocks), 2)
	eq_(len(blocks[0]), 16)
	eq_(len(blocks[1]), 16)

	text = b"Twelve Bytes" # 12 bytes = just one (not full) block
	blocks = get_blocks(text, 16)
	eq_(len(blocks), 1)
	eq_(len(blocks[0]), 12)

	text = b"Sixteen Byte MsgSixteen Byte MsgTwelve Bytes" # 44 bytes = 2 full blocks and a small block
	blocks = get_blocks(text, 16)
	eq_(len(blocks), 3)
	eq_(len(blocks[0]), 16)
	eq_(len(blocks[1]), 16)
	eq_(len(blocks[2]), 12)

def test_increment():
	bytes = b'abc'
	eq_(increment(b'abc'), b'abd')
	eq_(increment(b'\xFF'), b'\x01\x00')

def test_equal():
	tag1 = "\x00\x00\x00\x00\x00\x00"		# original tag
	tag2 = "\x00\x00\x00\x00\x00\x00"		# tag equal to original tag
	tag3 = "\x00\x00\x00\x00\x00\x01"		# slightly different
	tag4 = "\xFF\xFF\xFF\xFF\xFF\xFF"		# completely different
	tag5 = "\x00"							# too short
	tag6 = "\x00\x00\x00\x00\x00\x00\x00"	# too long

	assert_equal(tag1, tag2)
	assert_not_equal(tag1, tag3)
	assert_not_equal(tag1, tag4)
	assert_not_equal(tag1, tag5)
	assert_not_equal(tag1, tag6)