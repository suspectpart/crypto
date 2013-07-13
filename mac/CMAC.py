'''
CMAC
CMAC works almost the same way as the ECBC MAC. It needs three keys, the last plaintext block is
either xor'ed with k1 (if the message was padded) or k2 (if there are only full blocks) before
encrypting it with k.
'''
from crypto.utils import xor, get_blocks, mac_pad
from Crypto.Cipher import AES
from Base_Mac import Base_Mac

class CMAC(Base_Mac):
	def __init__(self, key):
		self.k, self.k1, self.k2 = key
		self.cipher = AES.new(self.k, AES.MODE_ECB)
		self.BLOCK_SIZE = self.cipher.block_size

	def sign(self, message):
		last_block_key = self.k2 if len(message) % self.BLOCK_SIZE == 0 else self.k1
		if last_block_key == self.k1:
			message = mac_pad(message, self.BLOCK_SIZE)

		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(message[:-self.BLOCK_SIZE], self.BLOCK_SIZE):
			tag = self.cipher.encrypt(xor(block, tag))

		last_block = message[-self.BLOCK_SIZE:]
		return self.cipher.encrypt(xor(last_block_key, xor(last_block, tag)))

	def verify(self, message, tag):
		return Base_Mac.verify(self, message, tag)