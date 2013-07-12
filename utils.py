from Crypto.Util.number import long_to_bytes, bytes_to_long

def get_blocks(text, block_size):
	full_blocks = len(text) / block_size
	blocks = [text[block_size * b: b * block_size + block_size] for b in range(0, full_blocks)]
	last_block = text[len(blocks) * block_size:] 
	if last_block:
		blocks.append(last_block)

	return blocks

def increment(bytestring):
	return long_to_bytes(bytes_to_long(bytestring) + 1)

def pad(text, block_size):
	padding_bytes = block_size - len(text) % block_size
	return text + b"".join([chr(padding_bytes)] * padding_bytes)

def unpad(text):
	return text[0:-ord(text[-1])]

def xor(block_x, block_y):
	return b"".join([chr(ord(a) ^ ord(b)) for a, b in zip(block_x, block_y)])

def equal(tag1, tag2):
	return sum((ord(x) ^ ord(y) for x,y in zip(tag1, tag2))) == 0