from crypto.utils import xor, get_blocks
import crypto.utils
from Crypto.Cipher import AES

class CBC_MAC(object):
	def __init__(self, key1, key2):
		self.cipher1 = AES.new(key1, AES.MODE_ECB)
		self.cipher2 = AES.new(key2, AES.MODE_ECB)
		self.BLOCK_SIZE = self.cipher1.block_size

	def generate_tag(self, message):
		message = crypto.utils.pad(message, self.BLOCK_SIZE)	# replace by the secure MAC pad
		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(message, self.BLOCK_SIZE):
			tag = self.cipher1.encrypt(xor(block, tag))

		return self.cipher2.encrypt(tag)

	def verify_tag(self, message, tag):
		return self.generate_tag(message) == tag

def pad(message, block_size):
	if len(message) % block_size == 0:
		message += b'\x80' + (block_size - 1) * '\x00'
	return message