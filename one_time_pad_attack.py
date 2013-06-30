'''
Example Attack on the integrity of the OTP

This attack assumes that we have some knowledge about what information the cipher carries.

We assume the last three letters of the cipher to be "bob" encrypted, 
as this is mail communication between alice and bob. 
If we xor the original cipher with some values we call p, we can achieve to change the message
of the decoded cipher c.

Usually, encoding means to create a cipher enc(m): c = m xor k.
Decoding this works by doing dec(c): dec(c xor k) = m.
If we now introduce p in the encryption, we get c = (m xor k) xor p.
Decrypting this results in dec(c) = dec(((m xor k) xor p)) xor k) = m xor p !

Let's introduce eve:

bob = 98  111  98
eve = 101 118 101
bob xor eve = 7 25 7  => the p we need to change bob to eve
'''

import one_time_pad

message = "hallobob"
key = one_time_pad.generate_key(message)
cipher = one_time_pad.encrypt(message,key)

tampered_cipher = []
tampered_cipher.append(chr(ord(cipher[-3]) ^ 7))
tampered_cipher.append(chr(ord(cipher[-2]) ^ 25))
tampered_cipher.append(chr(ord(cipher[-1]) ^ 7))
tampered_cipher = cipher[0:5] + "".join(tampered_cipher)


print "The original cipher: ", cipher
print "The tampered cipher: ", tampered_cipher 
print "Decryption of the original cipher: ", one_time_pad.decrypt(cipher,key)
print "Decryption of the changed cipher: ", one_time_pad.decrypt(tampered_cipher, key)