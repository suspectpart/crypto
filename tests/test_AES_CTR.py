from nose.tools import *
from crypto.homework.AES import *

def test_AES_CTR():
	key = b"Sixteen byte key"
	message = b"This is a very long message that should be encrypted and decrypted using CBC with a random IV" 
	sut = AES_CTR(key)
	eq_(sut.decrypt(sut.encrypt(message)), message)