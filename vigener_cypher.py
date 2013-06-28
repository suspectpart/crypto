import string

def vigener_cypher(key, message):
	alphabet = string.lowercase
	key *= (len(message) // len(key)) + 1
	translate = lambda x: [alphabet.index(c) for c in x]
	message, key = translate(message), translate(key)
	cypher = [(pair[0] + 1 + pair[1]) % 26 for pair in zip(key, message)]
	cypher = map(lambda c: alphabet[c], cypher)
	return ''.join(cypher)

key = "crypto"
message = "whatanicedaytoday"
expected_cypher = "zzzjucludtunwgcqs"
cypher = vigener_cypher(key, message)
print "c(",key,",",message,") := ", cypher 
assert cypher == expected_cypher