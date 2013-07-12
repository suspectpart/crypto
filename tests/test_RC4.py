from nose.tools import *
import key
from crypto.RC4 import *

def test_key_stream_generation():
	eq_(generate_keystream(b"Key", 10), b"EB9F7781B734CA72A719".decode("hex"))
	eq_(generate_keystream(b"Wiki", 6), b"6044DB6D41B7".decode("hex"))
	eq_(generate_keystream(b"Secret", 8), b"04D46B053CA87B59".decode("hex"))

def test_rc4_encryption():
	k = key.with_length(128)
	message = "Attack at dawn!"
	eq_(decrypt(encrypt(message, k), k), message)