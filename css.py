from nose.tools import *

'''
Content Scramble System
'''
import random

#Linear Feedback Shift Register
class LFSR(object):
	def __init__(self, seed, taps):
		self.register = [1] + seed # 1 append 1 to seed to avoid 0 cycling
		self.taps = taps

	def cycle(self):
		
		result = []
		for i in range(0,8):
			feedback_bit = reduce(lambda x,y: x ^ y, self.tap_bits())
			result.append(self.register.pop())
			self.register = [feedback_bit] + self.register

		output = 0
		for index, value in enumerate(result):
			output = output + value * (2 ** index)
		print output
		return output

	def tap_bits(self):
		return [self.register[tap] for tap in self.taps]

def encode(message, key):
	lfsr_1 = LFSR(key[0:16], [0,14]) # 17 bit LSFR
	lfsr_2 = LFSR(key[16:40], [10,18,19,22]) # 25 bit LSFR
	
if __name__ == "__main__":
	pass