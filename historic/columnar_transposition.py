'''
Example for a transposition cipher.
Given a message m and a keyword k, the cipher works as follow:

1) Every letter of the keyword is assigned a priority based
on its position in the alphabet relative to all other letters.
For k = "zebras" this would be:

zebras
632415

2) The message is first stripped of all non-alphabet characters
and padded with random letters to be a multiple of the keyword length.
So the message m = "we are discovered. flee at once." becomes
"wearediscoveredfleeatonce{r}5", r{5} meaning 5 random lettters appended as padding.

3) The message is written under the keyword in rows:

zebras

weared
iscove
redfle
eatonc
errrrr

4) Based on the assigned priorities, the ciphertext is read columnwise in blocks,
starting with the highest priority:

c = "evln[a-z] acdt[a-z] esea[a-z] rofo[a-z] deec[a-z] wiree"
'''

import string, math, random, re

def encrypt(message, keyword):
	plaintext = _pad(_normalize(message), keyword)
	key = _weighted(keyword)
	columns = _distribute_text_to_key_columns(plaintext, key)
	return _read_ciphertext_from(columns)

def _weighted(keyword):
	return [sorted(keyword).index(x) + 1 for x in keyword]

def _normalize(message):
	return re.sub("[^a-z]+", "", message)

def _pad(message, keyword):
	missing_bytes = len(keyword) - (len(message) % len(keyword))
	if missing_bytes == len(keyword):
		return message
	else:
		message += b"".join([string.lowercase[random.randint(0, 25)] for i in range(missing_bytes)])
	return message

def _distribute_text_to_key_columns(message, key):
	key = [(x, []) for x in key]
	for i, c in enumerate(message):
		key[i % len(key)][1].append(c)
	return key

def _read_ciphertext_from(key_columns):
	ciphertext = b""
	for column in sorted(key_columns):
		ciphertext += b"".join(column[1]) + b" "
	return ciphertext.strip()