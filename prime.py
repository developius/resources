import math

def isPrime(num): # returns True or False depending on if supplied number is prime
	if num < 2: return False # number is less than two so it's not prime
	for i in range(2, int(math.sqrt(num)) + 1): # for every number up until the number's sqrt
		if num % i == 0: return True # if it's divisible by two
	return False # otherwise
