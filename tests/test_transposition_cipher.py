from nose.tools import *
import string
import math

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
	assert_equal(padded_message[0:len(message)], message)

	message = b'manyzebras'
	padded_message = _pad(message, keyword)
	assert_equal(len(padded_message) % len(keyword), 0)
	assert_equal(padded_message[0:len(message)], message)

def test_should_add_message_to_key_columns():
	message = b'wearediscoveredfleeatonce'
	
	key = _distribute_message_to_key_columns(message, [6,3,2,4,1,5])

	assert_equal(key[0][1], ['w', 'i', 'r', 'e', 'e'])
	assert_equal(key[1][1], ['e', 's', 'e', 'a'])
	assert_equal(key[2][1], ['a', 'c', 'd', 't'])
	assert_equal(key[3][1], ['r', 'o', 'f', 'o'])
	assert_equal(key[4][1], ['e', 'v', 'l', 'n'])
	assert_equal(key[5][1], ['d', 'e', 'e', 'c'])

def test_should_create_cipher_text():
	key_columns = _distribute_message_to_key_columns(b'wearediscoveredfleeatonceqkjeu', [6,3,2,4,1,5])
	
	ciphertext = _read_ciphertext_from(key_columns)
	
	assert_equal(ciphertext, b"evlne acdtk eseaq rofoj deecu wiree")

def _weighted(keyword):
	return [sorted(keyword).index(x) + 1 for x in keyword]

def _normalize(message):
	return b"".join([c for c in message if c in string.lowercase])

def _pad(message, keyword):
	missing_bytes = len(keyword) - (len(message) % len(keyword))
	return message if missing_bytes == len(keyword) else message + (b'a' * missing_bytes)

def _distribute_message_to_key_columns(message, key):
	key = [(x, []) for x in key]
	for i, c in enumerate(message):
		key[i % len(key)][1].append(c)
	return key

def _read_ciphertext_from(key_columns):
	ciphertext = b""
	for column in sorted(key_columns):
		ciphertext += b"".join(column[1]) + b" "
	return ciphertext.strip()


'''
attack at dawn

ZEBRAS
632415

WEARED
ISCOVE
REDFLE
EATONC
EXXXXX
'''