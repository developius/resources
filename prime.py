import math

def isPrime(num): # returns True or False depending on if supplied number is prime
	if num < 2: return False # number is less than two so it's not prime
	for i in range(2, int(math.sqrt(num)) + 1): # for every number up until the number's sqrt
		if num % i == 0: return False # if it's divisible by two
	return True # otherwise

def primesUpTo(num): # returns list of primes up until num
	sieve = [True] * num
	sieve[0] = False # 0 and 1 are not prime
	sieve[1] = False
	for i in range(2, int(math.sqrt(num)) + 1): # loop through all numbers up until the sqrt of num
		pointer = i * 2
		while pointer < num:
			sieve[pointer] = False
			pointer += i
	primes = []
	for i in range(num):
		if sieve[i] == True: primes.append(i) # then it's a prime
	return primes # let's have the primes!
