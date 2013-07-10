from crypto.utils import xor, get_blocks
from Crypto.Cipher import AES

'''
Generates tags for messages using AES in CBC mode with two keys
'''
class CBC_MAC(object):
	def __init__(self, key1, key2):
		self.cipher1 = AES.new(key1, AES.MODE_ECB)
		self.cipher2 = AES.new(key2, AES.MODE_ECB)
		self.BLOCK_SIZE = self.cipher1.block_size

	def sign(self, message):
		message = pad(message, self.BLOCK_SIZE)	
		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(message, self.BLOCK_SIZE):
			tag = self.cipher1.encrypt(xor(block, tag))

		return self.cipher2.encrypt(tag)

	def verify(self, message, tag):
		return self.sign(message) == tag

'''
Secure padding for MAC tags
'''
def pad(message, block_size):
	bytes_to_pad = block_size - (len(message) % block_size) - 1
	return message + b'\x80' + bytes_to_pad * '\x00'