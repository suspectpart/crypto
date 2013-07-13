'''
Encrypted CBC MAC (using two keys) based on AES. 
It is crucial to encrypt the resulting tag again using a different key.
'''

from crypto.utils import xor, get_blocks, mac_pad
from Crypto.Cipher import AES
from Base_Mac import Base_Mac

class CBC_MAC(Base_Mac):
	def __init__(self, key):
		self.cipher1 = AES.new(key[0], AES.MODE_ECB)
		self.cipher2 = AES.new(key[1], AES.MODE_ECB)
		self.BLOCK_SIZE = self.cipher1.block_size

	def sign(self, message):
		message = mac_pad(message, self.BLOCK_SIZE)	
		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(message, self.BLOCK_SIZE):
			tag = self.cipher1.encrypt(xor(block, tag))

		return self.cipher2.encrypt(tag)

	def verify(self, message, tag):
		return Base_Mac.verify(self, message, tag)