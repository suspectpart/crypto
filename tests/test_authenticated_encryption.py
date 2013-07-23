from nose.tools import *
from mac.CBC_MAC import CBC_MAC
from AES_CBC import AES_CBC
from authenticated_encryption import Authenticated_Encryption
import key

def test_encryption_and_signing():
	message = "Some arbitrary message"
	mac_key_1 = key.with_length(256)
	mac_key_2 = key.with_length(256)
	cbc_key = key.with_length(256) 
	
	authenticated_encryption = Authenticated_Encryption((mac_key_1, mac_key_2, cbc_key))

	mac = CBC_MAC((mac_key_1, mac_key_2))
	cbc = AES_CBC(cbc_key)

	cipher, tag = authenticated_encryption.encrypt_and_sign(message)

	assert_equal(message, cbc.decrypt(cipher))
	assert_equal(tag, mac.sign(cipher))

def test_failing_authentication():
	message = "Some arbitrary message"
	mac_key_1 = key.with_length(256)
	mac_key_2 = key.with_length(256)
	cbc_key = key.with_length(256) 
	
	authenticated_encryption = Authenticated_Encryption((mac_key_1, mac_key_2, cbc_key))

	mac = CBC_MAC((mac_key_1, mac_key_2))
	cbc = AES_CBC(cbc_key)

	cipher, tag = authenticated_encryption.encrypt_and_sign(message)

	authenticated, decrypted_message = authenticated_encryption.authenticate_and_decrypt(cipher, "Wrong Tag")
	assert_equal(authenticated, False)
	assert_equal(decrypted_message, b"")

	authenticated, decrypted_message = authenticated_encryption.authenticate_and_decrypt("Wrong cipher", tag)
	assert_equal(authenticated, False)
	assert_equal(decrypted_message, b"")

def test_successfull_authentication_and_decryption():
	message = "Some arbitrary message"
	mac_key_1 = key.with_length(256)
	mac_key_2 = key.with_length(256)
	cbc_key = key.with_length(256) 
	
	authenticated_encryption = Authenticated_Encryption((mac_key_1, mac_key_2, cbc_key))

	mac = CBC_MAC((mac_key_1, mac_key_2))
	cbc = AES_CBC(cbc_key)

	cipher, tag = authenticated_encryption.encrypt_and_sign(message)
	authenticated, decrypted_message = authenticated_encryption.authenticate_and_decrypt(cipher, tag)
	assert_equal(authenticated, True)
	assert_equal(decrypted_message, message)

