from nose.tools import *
from crypto.RC4 import *

def test_key_stream_generation():
	eq_(generate_keystream(b"Key", 10), b"EB9F7781B734CA72A719".decode("hex"))
	eq_(generate_keystream(b"Wiki", 6), b"6044DB6D41B7".decode("hex"))
	eq_(generate_keystream(b"Secret", 8), b"04D46B053CA87B59".decode("hex"))

def test_rc4_encryption():
	key = "secret key"
	message = "Attack at dawn!"
	eq_(encrypt(encrypt(message,key), key), message)