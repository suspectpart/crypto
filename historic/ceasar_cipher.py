import string

def caesar_cypher(message, rotations):
	alphabet = string.lowercase
	rotate = lambda x: (x + rotations) % len(alphabet)  
	cypher = [rotate(alphabet.index(c)) for c in message]
	return "".join(map(lambda c: alphabet[c], cypher))

rotations = 3
message, expected_cypher = "hallo", "kdoor"
assert caesar_cypher(message, rotations) == expected_cypher