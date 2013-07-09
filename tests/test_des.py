from nose.tools import *
from DES import *

def test_neighbour():
	assert neighbour(0) == 47
	assert neighbour(4) == 5
	assert neighbour(8) == 11
	assert neighbour(28) == 41

def test_get_sbox_value():
	assert get_from_sbox(0, BitArray('0b101110')) == BitArray('0b1011')
	assert get_from_sbox(1, BitArray('0b000000')) == BitArray('0b1111')
	assert get_from_sbox(2, BitArray('0b111111')) == BitArray('0b1100')
	assert get_from_sbox(7, BitArray('0b100000')) == BitArray('0b0111')

def test_expand():
	block = range(0,32)
	output = expand(block)

	assert block[0] == output[1] == output[47]
	assert block[1] == output[2]
	assert block[2] == output[3]
	assert block[3] == output[4] == output[6]

#	assert block[4] == output[7] == output[5]
	assert block[5] == output[8]
	assert block[6] == output[9]
	assert block[7] == output[10] == output[12]
	
#	assert block[8] == output[13] == output[11]
	assert block[9] == output[14]
	assert block[10] == output[15]
	assert block[11] == output[16] == output[18]
	
#	assert block[12] == output[19] == output[17]
	assert block[13] == output[20]
	assert block[14] == output[21]
	assert block[15] == output[22] == output[24]

#	assert block[16] == output[25] == output[23]
	assert block[17] == output[26]
	assert block[18] == output[27]
	assert block[19] == output[28] == output[30]

#	assert block[20] == output[31] == output[29]
	assert block[21] == output[32]
	assert block[22] == output[33]
	assert block[23] == output[34] == output[36]

#	assert block[24] == output[37] == output[35]
	assert block[25] == output[38]
	assert block[26] == output[39]
	assert block[27] == output[40] == output[42]

#	assert block[28] == output[43] == output[41]
	assert block[29] == output[44]
	assert block[30] == output[45]
	assert block[31] == output[46] == output[0]
