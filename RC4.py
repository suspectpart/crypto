def generate_keystream(key, length):
	s_box = generate_sbox(key)
	i = j = 0
	key_stream = b''

	while length > 0:
		i = (i + 1) % 256
		j = (j + s_box[i]) % 256
		s_box[i], s_box[j] = s_box[j], s_box[i]
		key_stream += chr(s_box[(s_box[i] + s_box[j]) % 256])
		length -= 1

	return key_stream

def generate_sbox(key):
	s_box = range(0, 256)
	j = 0

	for i, value in enumerate(s_box):
		j = (j + value + ord(key[i % len(key)])) % 256
		s_box[i], s_box[j] = s_box[j], s_box[i]

	return s_box