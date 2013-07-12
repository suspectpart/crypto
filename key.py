import random

def with_length(bits):
	return b"".join([chr(random.getrandbits(8)) for x in range(bits / 8)])