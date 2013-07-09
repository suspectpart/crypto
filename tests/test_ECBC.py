from ECBC import CBC_MAC

def test_cbc_mac():
	key1 = "001122334455667788"
	key2 = "FFXXAABBCCDDEEFF00"
	message = "Secret Message"
	cbc_mac = CBC_MAC(key1, key2)
	tag = cbc_mac.generate_tag(message)
	eq_(cbc_mac.verify_tag(message, tag), True) 
	eq_(cbc_mac.verify_tag(message, "Wrong Tag"), True) 
	eq_(cbc_mac.verify_tag("Wrong Message", tag), False) 