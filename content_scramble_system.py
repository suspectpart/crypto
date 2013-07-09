'''
Content Scramble System

The Content Scramble System (CSS) uses two LFSRs and a 5 byte key.
The 5 byte key is divided into 2 bytes as the seed for the first LFSR
and 3 bytes as the seed for the second LFSR. Also the taps have to be defined.

For every byte of the input message both LFSRs perform a cycle that outputs a byte.
Those bytes are added together mod 256, the carry is thrown away.
Doing this for every byte of the input creates a key stream that is used to
encrypt the whole input message.
'''
from crypto.lfsr import LFSR
import random

def encode(message, key):
	lfsr_1 = LFSR(key[0:16], [0,14]) # 17 bit LSFR
	lfsr_2 = LFSR(key[16:40], [10,18,19,22]) # 25 bit LSFR
	
	cipher = []

	for character in message:
		key_stream = (lfsr_1.cycle() + lfsr_2.cycle()) % 256
		cipher.append(key_stream ^ ord(character))
		
	return "".join(map(chr, cipher))

if __name__ == "__main__":
	message = "secretmessage"
	key = [1,0,1,0,1,0,1,0] * 2 + [0,1,0,1,0,1,0,1] * 3
	cipher = encode(message, key)
	decrypted_text = encode(cipher, key)

	print "Message:", message
	print "Cipher: ", cipher
	print "Decrypted Text: ", decrypted_text 