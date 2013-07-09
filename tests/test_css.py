from nose.tools import *
import random
import crypto.content_scramble_system

def test_css():
	message = "secretmessage"
	key = [random.getrandbits(1) for i in range(0,40)]
	cipher = crypto.content_scramble_system.encode(message, key)
	decrypted_text = crypto.content_scramble_system.encode(cipher, key)
	assert cipher != message
	assert message == decrypted_text