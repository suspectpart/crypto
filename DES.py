from nose.tools import *
from bitstring import BitArray


# expand 32-bit block to 48-bit block
def expand(block):
	new_block = BitArray()
	map = lambda x: x + (((x-1) / 4) * 2) + 1
	return 0

# get 4-bit substitution for 6-bit block in S-Box x
def get_from_sbox(box, block):
	offset = (BitArray([block[0], block[-1]]).uint * 16) + BitArray(block[1:5]).uint
	return BitArray(hex(__sbox[box][offset]))

def test_expand():
	pass

def test_get_sbox_value():
	assert get_from_sbox(0, BitArray('0b101110')) == BitArray('0b1011')
	assert get_from_sbox(1, BitArray('0b000000')) == BitArray('0b1111')
	assert get_from_sbox(2, BitArray('0b111111')) == BitArray('0b1100')
	assert get_from_sbox(7, BitArray('0b100000')) == BitArray('0b0111')

def test_expand():
	block = BitArray([hex(x) for x in range(0,32)])
	output = expand(block)
	assert block[0] == output[1] == output[47]
	assert block[1] == output[2]
	assert block[2] == output[3]
	assert block[3] == output[4] == output[6]

	assert block[4] == output[7] == output[5]
	assert block[5] == output[8]
	assert block[6] == output[9]
	assert block[7] == output[10] == output[12]
	
	assert block[8] == output[13] == output[11]
	assert block[9] == output[14]
	assert block[10] == output[15]
	assert block[11] == output[16] == output[18]
	
	assert block[12] == output[19] == output[17]
	assert block[13] == output[20]
	assert block[14] == output[21]
	assert block[15] == output[22] == output[24]

	assert block[16] == output[25] == output[23]
	assert block[17] == output[26]
	assert block[18] == output[27]
	assert block[19] == output[28] == output[30]

	assert block[20] == output[31] == output[29]
	assert block[21] == output[32]
	assert block[22] == output[33]
	assert block[23] == output[34] == output[36]

	assert block[24] == output[37] == output[35]
	assert block[25] == output[38]
	assert block[26] == output[39]
	assert block[27] == output[40] == output[42]

	assert block[28] == output[43] == output[41]
	assert block[29] == output[44]
	assert block[30] == output[45]
	assert block[31] == output[46] == output[0]

__sbox = [
	# S1
	[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
	 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
	 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
	 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

	# S2
	[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
	 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
	 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
	 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

	# S3
	[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
	 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
	 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
	 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

	# S4
	[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
	 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
	 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
	 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

	# S5
	[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
	 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
	 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
	 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

	# S6
	[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
	 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
	 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
	 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

	# S7
	[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
	 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
	 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
	 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

	# S8
	[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
	 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
	 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
	 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]