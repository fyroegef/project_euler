import numpy as np

def isPrime(num):
	if num == 2:
		return True
	max_val = int(np.ceil(np.sqrt(num))+1)
	for x in range(2,max_val):
		if num%x == 0:
			return False
	return True

def numbPrime(number=6):
	test_val = 2
	num_of_primes = 0
	while True:
		if isPrime(test_val):
			num_of_primes += 1
			if num_of_primes == number:
				return test_val
		test_val += 1