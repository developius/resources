# Adaption of http://inventwithpython.com/simpleSubCipher.py
import sys, random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getRandomKey():
	key = list(ALPHABET)
	random.shuffle(key)
	return(''.join(key))

def checkKey(key):
	key = key.upper()
	keyList = list(key)
	ALPHABETList = list(ALPHABET)
	keyList.sort()
	ALPHABETList.sort()
	if keyList != ALPHABETList: sys.exit('Key requires every letter in the alphabet x1')

def decrypt(key, message):
	decrypted = ""
	charsA = ALPHABET
	charsB = key
	charsA, charsB = charsB, charsA
	for c in message:
		if c.upper() in charsA:
			cIndex = charsA.find(c.upper())
			if c.isupper(): decrypted += charsB[cIndex].upper()
			else: decrypted += charsB[cIndex].lower()
		else: decrypted += c
	return(decrypted)

def encrypt(key, message):
	encrypted = ""
	charsA = ALPHABET
	charsB = key
	for c in message:
		if c.upper() in charsA:
			cIndex = charsA.find(c.upper())
			if c.isupper(): encrypted += charsB[cIndex].upper()
			else: encrypted += charsB[cIndex].lower()
		else: encrypted += c
	return(encrypted)
