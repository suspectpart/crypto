from nose.tools import *
import key

def test_new_key():
	k1 = key.with_length(128)
	k2 = key.with_length(128)
	assert_equal(len(k1), 16)
	assert_equal(len(k2), 16)
	assert_not_equal(k1, k2)