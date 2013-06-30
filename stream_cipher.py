'''
Example of a Stream Cipher

Instead of creating a random key that is as long as the message to be encrypted (= OTP),
a stream cipher just takes a small key (=seed) that is put into a PRG (Pseudo Random Generator)
to create a non-predictable, infinite stream of key-bits. 

It is deterministic that every seed will produce the same stream of bits, 
but no bit can be predicted by looking at any other bits in the stream.

As the key in most cases will be smaller than the message, in theory a stream cipher
does not have perfect secrecy 
(perfect secrecy means that the key space is at least the size of the message space 
and that every message could be encrypted by any key available)
'''

import random

def encrypt(message, key):
	key_stream = create_key_stream(message, key)
	cipher = [pair[0] ^ ord(pair[1]) for pair in zip(key_stream, message)]
	return "".join(map(chr, cipher))

def decrypt(cipher, key):
	return encrypt(cipher, key)

def create_key_stream(text, key):
	prg = random.Random()
	prg.seed(key)
	return (prg.getrandbits(8) for c in text)

if __name__ == "__main__":
	key = 0xEE
	message = "hallowelt"
	cipher = encrypt(message, key)
	decrypted_message = decrypt(cipher, key)
	assert decrypted_message == message
	print "Key: ", key, ", Message: ", message, ", Cipher: ", cipher