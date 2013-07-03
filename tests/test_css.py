from nose.tools import *
import random
import content_scramble_system

def test_css():
	message = "secretmessage"
	key = [random.getrandbits(1) for i in range(0,40)]
	cipher = content_scramble_system.encode(message, key)
	decrypted_text = content_scramble_system.encode(cipher, key)
	assert cipher != message
	assert message == decrypted_text