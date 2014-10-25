import string

def encrypt(text,shift):
	cipher = ""
	for char in text:
		c = (ord(char)+shift) % 126
		if c < 32: c+=31
		cipher += chr(c)
	return(cipher)

def decrypt(text,shift):
	plaintext = ""
	for char in text:
		p = (ord(char)-shift) % 126
		if p < 32: p+=95				
		plaintext += chr(p)
	return(plaintext)
