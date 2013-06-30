from nose.tools import *
from lfsr import LFSR

def test_cycle():
	'''
	First cycle:
	1,1,0,1,0 -> output 0, feedback 0
	0,1,1,0,1 -> output 1, feedback 1
	1,0,1,1,0 -> output 0, feedback 1
	1,1,0,1,1 -> output 1, feedback 0
	0,1,1,0,1 -> output 1, feedback 1
	1,0,1,1,0 -> output 0, feedback 1
	1,1,0,1,1 -> output 1, feedback 0
	0,1,1,0,1 -> output 1, feedback 1
	
	Output = 11011010b = 128d
	'''
	lfsr = LFSR([1,0,1,0], [0,1])
	output = lfsr.cycle()
	assert output == 218