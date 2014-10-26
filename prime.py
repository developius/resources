import math

def isPrime(num): # returns True or False depending on if supplied number is prime
	if num < 2: return False # number is less than two so it's not prime
	for i in range(2, int(math.sqrt(num)) + 1): # for every number up until the number's sqrt
		if num % i == 0: return False # if it's divisible by two
	return True # otherwise

def primeSieve(sieveSize):
	sieve = [True] * sieveSize
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(math.sqrt(sieveSize)) + 1):
		pointer = i * 2
		while pointer < sieveSize:
			sieve[pointer] = False
			pointer += i
	primes = []
	for i in range(sieveSize):
		if sieve[i] == True: primes.append(i)
	return primes
