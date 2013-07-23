'''
Cipher Block Chaining (CBC) with a random Initialization Vector (IV) using AES.
When encrypting, a random initial IV is chosen with the size of one block. 
Then for every block in the plaintext one round of encryption is performed where the IV 
is xor'ed with the plaintext block and encrypted using AES. 
The resulting ciphertext block becomes the new IV for the next round and so on. 
The initial IV is prepended to the resulting ciphertext.

Decryption works almost the same way. The IV is taken from the ciphertext and all the rounds are performed,
this time with AES decryption and xor'ing IV and textblock after decryption.
'''

from Crypto.Cipher import AES
from Crypto import Random
from crypto.utils import *

class AES_CBC(object):
	def __init__(self, key):
		self.cipher = AES.new(key, AES.MODE_ECB)
		self.key = key
		self.BLOCK_SIZE = self.cipher.block_size

	def encrypt(self, plaintext):
		iv = Random.new().read(self.BLOCK_SIZE)
		plaintext = pad(plaintext, self.BLOCK_SIZE)
		ciphertext = iv

		for block in get_blocks(plaintext, self.BLOCK_SIZE):
			cipher_block = self.cipher.encrypt(xor(block, iv))
			ciphertext += cipher_block
			iv = cipher_block	# set iv to cipher block of previous encryption = CBC!

		return ciphertext

	def decrypt(self, ciphertext):
		iv = ciphertext[0:self.BLOCK_SIZE]
		plaintext = b""

		for cipher_block in get_blocks(ciphertext[self.BLOCK_SIZE:], self.BLOCK_SIZE):	# skip iv
			plaintext_block = xor(self.cipher.decrypt(cipher_block), iv)
			plaintext += plaintext_block
			iv = cipher_block	# set iv to plaintext block of previous decryption = CBC!

		return unpad(plaintext)