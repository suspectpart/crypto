'''
The Vigener cypher

A basic cipher example. A certain key is chosen and duplicated many times
until the length of the key reaches the length of the message.

The message is than encrypted by adding the alphabetical value (a = 1, b = 2..)
of the key to the alphabetical value of the message for any bit mod 26 (y + c = b)

Guessing the length of the key, this encryption might be broken by dividing
the cipher into chunks, looking at the first letter in every chunk and apply
letter frequencies
'''

import string

def vigener_cipher(key, message):
	alphabet = string.lowercase
	key *= (len(message) // len(key)) + 1
	translate = lambda x: [alphabet.index(c) for c in x]
	message, key = translate(message), translate(key)
	cipher = [(pair[0] + 1 + pair[1]) % 26 for pair in zip(key, message)]
	cipher = map(lambda c: alphabet[c], cipher)
	return ''.join(cipher)

key = "crypto"
message = "whatanicedaytoday"
expected_cipher = "zzzjucludtunwgcqs"
cipher = vigener_cipher(key, message)
print "c(",key,",",message,") := ", cipher 
assert cipher == expected_cipher