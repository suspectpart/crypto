from nose.tools import *
from columnar_transposition import encrypt, _pad, _normalize, _distribute_text_to_key_columns, _weighted, _read_ciphertext_from
import re

def test_should_strip_all_non_letter_characters_from_message():
	message = b'we are discovered. flee at once.'
	assert_equal(_normalize(message), b"wearediscoveredfleeatonce")

def test_should_return_same_message_if_only_letters():
	message = b'hallowelt'
	assert_equal(_normalize(message), message)

def test_should_return_empty_message():
	message = b''
	assert_equal(_normalize(message), message)

def test_should_weight_empty_keyword():
	keyword = b''
	weight = []
	assert_equal(weight, [])

def test_should_weight_one_letter_keyword():
	assert_equal(_weighted(b'a'), [1])
	assert_equal(_weighted(b'm'), [1])
	assert_equal(_weighted(b'z'), [1])

def test_should_weight_two_letter_keyword():
	assert_equal(_weighted(b'ab'), [1,2])
	assert_equal(_weighted(b'ba'), [2,1])
	assert_equal(_weighted(b'za'), [2,1])
	assert_equal(_weighted(b'az'), [1,2])
	assert_equal(_weighted(b'rm'), [2,1])

def test_should_weight_many_letter_keyword():
	keyword = b'zebras'
	assert_equal(_weighted(keyword), [6,3,2,4,1,5])

def test_should_not_pad_message_with_length_multiple_of_key():
	keyword = b'zebras'
	message = b'zebras'

	padded_message = _pad(message, keyword)
	assert_equal(message, padded_message)

def test_should_pad_message_with_length_not_multiple_of_key():
	keyword = b'zebras'
	message = b'hallo'
	padded_message = _pad(message, keyword)
	assert_equal(len(padded_message), len(keyword))
	assert_not_equal(None, re.match(message + "[a-z]", padded_message))

	message = b'manyzebras'
	padded_message = _pad(message, keyword)
	assert_equal(len(padded_message) % len(keyword), 0)
	assert_equal(padded_message[0:len(message)], message)

def test_should_add_message_to_key_columns():
	message = b'wearediscoveredfleeatonce'
	
	key = _distribute_text_to_key_columns(message, [6,3,2,4,1,5])

	assert_equal(key[0][1], ['w', 'i', 'r', 'e', 'e'])
	assert_equal(key[1][1], ['e', 's', 'e', 'a'])
	assert_equal(key[2][1], ['a', 'c', 'd', 't'])
	assert_equal(key[3][1], ['r', 'o', 'f', 'o'])
	assert_equal(key[4][1], ['e', 'v', 'l', 'n'])
	assert_equal(key[5][1], ['d', 'e', 'e', 'c'])

def test_should_create_cipher_text_from_key_columns():
	key_columns = _distribute_text_to_key_columns(b'wearediscoveredfleeatonceqkjeu', [6,3,2,4,1,5])
	
	ciphertext = _read_ciphertext_from(key_columns)
	
	assert_equal(ciphertext, b"evlne acdtk eseaq rofoj deecu wiree")

def test_should_do_whole_encryption():	
	ciphertext = encrypt(b"we are discovered. flee at once.", b"zebras")
	assert None != re.match("evln[a-z] acdt[a-z] esea[a-z] rofo[a-z] deec[a-z] wiree", ciphertext)