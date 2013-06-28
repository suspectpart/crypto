import random

def generate_key(message):
	return [random.getrandbits(8) for c in message]

def encrypt(message, key):
	return [ord(pair[0]) ^ pair[1] for pair in zip(message, key)]

def decrypt(cipher, key):
	return "".join([chr(pair[0] ^ pair[1]) for pair in zip(cipher, key)])
	

if __name__ == "__main__":
	message = "hallo"
	key = generate_key(message)
	cipher = encrypt(message, key)
	deciphered_text = decrypt(cipher, key)
	print "message: ", message
	print "key: ", key
	print "cipher: ", cipher
	print "decrypted message: ", deciphered_text 