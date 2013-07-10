from crypto.utils import xor, get_blocks
from Crypto.Cipher import AES
import random

'''
Encrypted CBC MAC (using two keys) based on AES.
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

class CMAC(object):
	def __init__(self, keys):
		self.k, self.k1, self.k2 = keys
		self.cipher = AES.new(self.k, AES.MODE_ECB)
		self.BLOCK_SIZE = self.cipher.block_size

	def sign(self, message):
		last_block_key = self.k2 if len(message) % self.BLOCK_SIZE == 0 else self.k1
		if last_block_key == self.k1:
			message = pad(message, self.BLOCK_SIZE)

		tag = b'\x00' * self.BLOCK_SIZE

		for block in get_blocks(message[:-self.BLOCK_SIZE], self.BLOCK_SIZE):
			tag = self.cipher.encrypt(xor(block, tag))

		last_block = message[-self.BLOCK_SIZE:]
		return AES.new(last_block_key, AES.MODE_ECB).encrypt(xor(last_block, tag))

	def verify(self, message, tag):
		return self.sign(message) == tag

'''
One Time MAC based on a polynomial with a message and two primes (a, b) from a big int space q. 
Secure for exactly one message, as sign(key, msg1) doesn't reveal anything about sign(key, msg2)
'''
class One_Time_Mac(object):
	def __init__(self):
		self.q = (2 ** 128) + 51

	def new_key(self):
		return (random.randint(1, self.q), random.randint(1, self.q))

	def sign(self, message, key):	
		a, b = key
		return (self._polynomial(message, a) + b) % self.q

	def verify(self, message, key, tag):
		return self.sign(message, key) == tag

	def _polynomial(self, message, x):
		p = x ** (len(message) + 1)
		for i, block in enumerate(message):
			p += (ord(block) * (x ** (i+1)))
		return p

'''
Secure padding for MAC tags
'''
def pad(message, block_size):
	bytes_to_pad = block_size - (len(message) % block_size) - 1
	return message + b'\x80' + bytes_to_pad * '\x00'