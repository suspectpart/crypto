'''
One Time MAC based on a polynomial with a message and two primes (a, b) from a big int space q. 
Secure for exactly one message, as sign(key, msg1) doesn't reveal anything about sign(key, msg2)
'''

import random

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