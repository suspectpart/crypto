''' 
Part of the discrete probability crash course
Uniform distribution means to determine a probability with which certain events are going to happen.
For example when rolling a dice with numbers 1-6 the probability for a number to turn up is P(number) = 1/6.
The probability for any number in [1,2,3] to turn up would be P(1,2,3) = 0.5
The probability for a 7 to turn up is P(7) = 0
The probability for any number from 1-6 to turn up is P(1,2,3,4,5,6) = 1.

Independent probabilities can be combined by addition. 
E.g. the chances to roll an odd number is P(1) + P(3) + P(5) = 1/6 + 1/6 + 1/6 = 3/6 = 0.5

Independent probabilities can be multiplied to represent the probability of successive events:
E.g. if 3 people roll a dice, the chance for all of them to roll a 6 is P(6) * P(6) * P(6) = 1/6 * 1/6 * 1/6 = 0,00463
'''

class uniform_distribution(object):
	def __init__(self, universe):
		self.universe = universe
	
	def probability(self, event):
		return len(event) / float(len(self.universe)) if self.valid(event) else 0
				
	def probability_complement(self, event):
		return 1 - self.probability(event) if self.valid(event) else 0
		
	def valid(self, event):
		return [e for e in event if e in self.universe] == event
		
if __name__ == '__main__':
	CERTAIN_EVENT = [3,2,1,6,5,4]	# certain event will happen with a probability of 1
	IMPOSSIBLE_EVENT = [7]			# impossible event will happen with a probability of 0
	
	d = uniform_distribution([1,2,3,4,5,6])
	
	print d.probability(CERTAIN_EVENT)
	print d.probability(IMPOSSIBLE_EVENT)
	print d.probability([1])
	print d.probability([1,3,6])
	print d.probability([1,2,3,4])
     
	print d.probability_complement(CERTAIN_EVENT)
	print d.probability_complement(IMPOSSIBLE_EVENT)
	print d.probability_complement([1])
	print d.probability_complement([1,2,3])
	 
	print d.probability([1]) + d.probability([3]) + d.probability([5])  # rolling an odd number
	print d.probability([6]) ** 3 # rolling a six three times in a row