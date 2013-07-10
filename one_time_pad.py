'''
Basic example of One Time Pad (OTP) encryption / decryption 

For every message, a randomly generated key is used that has to be exactly
as long as the message itself (which gives us perfect secrecy as the key space
is at least the size of the message space.)

A message is encrypted by xor-ing every bit of the message with every bit of the key,
returning the cipher text string. 
To decrypt the cipher, it just has to be xor-ed with the key again.

If the key is truly random and only used once, the OTP is completely unbreakable.
This is because for any ciphertext, all possible plaintext messages are equally likely.
So if you have you have a 5 character cipher, any word with 5 letters
is equally likely to be the original plain text message.
'''

from crypto.utils import xor
import random

def generate_key(message):
	return b"".join([chr(random.getrandbits(8)) for c in message])

def encrypt(message, key):
	return xor(message, key)

def decrypt(cipher, key):
	return encrypt(cipher, key)
	

if __name__ == "__main__":
	message = "hallo"
	key = generate_key(message)
	cipher = encrypt(message, key)
	deciphered_text = decrypt(cipher, key)
	print "message:\t", message
	print "key:\t\t", key.encode("hex")
	print "cipher:\t\t", cipher.encode("hex")
	print "decrypted:\t", deciphered_text 