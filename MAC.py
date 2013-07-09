from crypto.utils import pad, get_blocks, xor
from Crypto.Cipher import AES

class CBC_MAC(object):
	def __init__(self, key1, key2):
		self.cipher1 = AES.new(key1, AES.MODE_ECB)
		self.cipher2 = AES.new(key2, AES.MODE_ECB)
		self.BLOCK_SIZE = 16

	def generate_tag(self, message):
		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(pad(message, self.BLOCK_SIZE), self.BLOCK_SIZE):
			tag = self.cipher1.encrypt(xor(block, tag))

		return self.cipher2.encrypt(tag)

	def verify_tag(self, message, tag):
		return self.generate_tag(message) == tag