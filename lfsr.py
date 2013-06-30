'''
Linear Feedback Shift Register  
'''
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
		return output

	def tap_bits(self):
		return [self.register[tap] for tap in self.taps]
