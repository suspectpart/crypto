from Crypto.Cipher import AES
from Crypto import Random
from crypto.utils import *

class AES_CTR(object):
	def __init__(self, key):
		self.cipher = AES.new(key, AES.MODE_ECB)
		self.key = key
		self.BLOCK_SIZE = self.cipher.block_size

	def encrypt(self, plaintext):
		iv = Random.new().read(self.BLOCK_SIZE)
		ciphertext = iv

		for plaintext_block in get_blocks(plaintext, self.BLOCK_SIZE):
			cipher_block = xor(self.cipher.encrypt(iv), plaintext_block)
			ciphertext += cipher_block
			iv = increment(iv)	# set iv to cipher block of previous encryption = CBC!
		
		return ciphertext

	def decrypt(self, ciphertext):
		iv = ciphertext[0:self.BLOCK_SIZE]
		plaintext = b""

		for cipher_block in get_blocks(ciphertext[self.BLOCK_SIZE:], self.BLOCK_SIZE):	# skip iv
			plaintext_block = xor(self.cipher.encrypt(iv), cipher_block)
			plaintext += plaintext_block
			iv = increment(iv)	# set iv to plaintext block of previous decryption = CBC!
		
		return plaintext
