from nose.tools import *
import random
import css

def test_css():
	message = "secretmessage"
	key = [random.getrandbits(1) for i in range(0,40)]
	cipher = css.encode(message, key)
	decrypted_text = css.encode(cipher, key)
	assert cipher != message
	assert message == decrypted_text