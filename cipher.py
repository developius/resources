# -*- coding: utf-8 -*-
import sys
import random
import string


class Caesar:

    def __init__(self):
        pass

    def encrypt(self, text, shift):
        cipher = ""
        for char in text:
            if char.isalpha():
                num = ord(char)
                num += shift
                if char.isupper():
                    if num > ord('Z'):
                        num -= 26
                    else:
                        num += 26
                else:
                    if num > ord('Z'):
                        num -= 26
                    else:
                        num += 26
                cipher += chr(num)
            else:
                cipher += char
        return(cipher)

    def decrypt(self, text, shift):
        plaintext = ""
        for char in text:
            p = (ord(char) - shift) % 126
            if p < 32:
                p += 95
            plaintext += chr(p)
        return(plaintext)


class Morse:

    def __init__(self):
        self.codes = {"a": ".-", "b": "--...", "c": "-.-.", "d": "--..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "--..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                      "6": "-....", "7": "--....", "8": "---..", "9": "----.", "0": "-----", " ": "/", ".": ".-.-.-", ",": "--..--", "?": "..--..", "-": "..--..", "=": "-...-", ":": "---...", ";": "-.-.-.", "(": "-.--.", ")": "-.--.-", "/": "-..-.", "\"": ".-..-.", "$": "...-..-", "'": ".----.", "¶": ".-.-..", "_": "..--.-", "@": ".--.-.", "!": "---.", "+": ".-.-.", "~": ".-...", "&": ". ...", "//": "-..-.", "\#": "...-.-"}

    def encrypt(self, text):
        text = text.lower()
        toReturn = []
        for c in text:
            try:
                toReturn.append(self.codes[c])
            except:
                pass
        return(" ".join(toReturn))

    def decrypt(self, text):
        toReturn = []
        text = text.split(" ")
        for code in text:
            for key, val in self.codes.iteritems():
                if val == code:
                    toReturn.append(key)
        return("".join(toReturn).replace("/", " ").upper())


# Adaption of http://inventwithpython.com/simpleSubCipher.py
class Substitution:

    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def getRandomKey(self):
        key = list(self.alphabet)
        random.shuffle(key)
        return(''.join(key))

    def checkKey(self, key):
        key = key.upper()
        keyList = list(key)
        self.alphabetList = list(self.alphabet)
        keyList.sort()
        self.alphabetList.sort()
        if keyList != self.alphabetList:
            sys.exit('Key requires every letter in the alphabet x1')

    def decrypt(self, message, key):
        decrypted = ""
        for c in message:
            if c.upper() in key:
                cIndex = key.find(c.upper())
                if c.isupper():
                    decrypted += self.alphabet[cIndex].upper()
                else:
                    decrypted += self.alphabet[cIndex].lower()
            else:
                decrypted += c
        return(decrypted)

    def encrypt(self, message, key):
        encrypted = ""
        charsA = self.alphabet
        charsB = key
        for c in message:
            if c.upper() in charsA:
                cIndex = charsA.find(c.upper())
                if c.isupper():
                    encrypted += charsB[cIndex].upper()
                else:
                    encrypted += charsB[cIndex].lower()
            else:
                encrypted += c
        return(encrypted)
