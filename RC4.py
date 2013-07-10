def generate_keystream(key, length):
	s_box = _generate_sbox(key)
	i = j = 0
	key_stream = b''

	while length > 0:
		i = (i + 1) % 256
		j = (j + s_box[i]) % 256
		s_box[i], s_box[j] = s_box[j], s_box[i]
		key_stream += chr(s_box[(s_box[i] + s_box[j]) % 256])
		length -= 1

	return key_stream

def _generate_sbox(key):
	s_box = range(256)
	j = 0

	for i, value in enumerate(s_box):
		j = (j + value + ord(key[i % len(key)])) % 256
		s_box[i], s_box[j] = s_box[j], s_box[i]

	return s_box

def encrypt(message, key):
	xor = lambda x, y: chr(ord(x) ^ ord(y))
	key_stream = generate_keystream(key, len(message))
	return b"".join([xor(m,k) for m,k in zip(message, key_stream)])

def decrypt(ciphertext, key):
	return encrypt(ciphertext, key)

if __name__ == "__main__":
	message, key = "Attack at dawn!", "Secret Key"
	print message, " x ", key, " = ", encrypt(message, key).encode("hex")