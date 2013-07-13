from nose.tools import *
from crypto.mac.One_Time_Mac import One_Time_Mac

def test_one_time_mac():
	message = b"Attack at dawn!"
	one_time_mac = One_Time_Mac()
	key = one_time_mac.new_key()
	tag = one_time_mac.sign(message, key)
	ok_(one_time_mac.verify(message, key, tag))
	eq_(one_time_mac.sign("\x01\x01", (1,1)), (1 ** 3 + 1 * 1 ** 1 + 1) + 1 % 1000)