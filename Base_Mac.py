class Base_Mac(object):
	def __init__(self, key):
		self.key = key

	def sign(self, message):
		pass

	# prevents timing-attacks by comparing byte-by-byte, always taking the same time
	def verify(self, message, tag):
		return sum((ord(x) ^ ord(y) for x,y in zip(self.sign(message), tag))) == 0 