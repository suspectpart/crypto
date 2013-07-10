from nose.tools import *
from crypto.one_time_pad import *

def test_encrypt_decrypt():
	message = "Hallo, Welt!"
	key = generate_key(message)

	assert key != message
	eq_(len(key), len(message))
	eq_(decrypt(encrypt(message, key), key), message)