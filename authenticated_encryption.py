'''
Example implementation of authenticated encryption using a CBC-MAC and an AES-CBC cipher.

Every message is encrypted using AES-CBC. In the next step, a MAC is created by signing the ciphertext.
The abstract way here is Encrypt-Then-Mac, which should be the authenticated encryption mode to use. 

In the authentication and decryption step first the tag is verified and rejected if it is not valid
for the given ciphertext. This prevents any attacker from submitting any changed / tampered with 
ciphertexts of his / her choice.  
'''

from mac.CBC_MAC import CBC_MAC
from AES_CBC import AES_CBC

class Authenticated_Encryption(object):
	def __init__(self, keys):
		self.mac = CBC_MAC((keys[0], keys[1]))
		self.aes_cbc = AES_CBC(keys[2])

	def encrypt_and_sign(self, message):
		cipher = self.aes_cbc.encrypt(message)
		tag = self.mac.sign(cipher)
		return cipher, tag

	def authenticate_and_decrypt(self, cipher, tag):
		authenticated = self.mac.verify(cipher, tag)
		message = "" if not authenticated else self.aes_cbc.decrypt(cipher)
		
		return authenticated, message
