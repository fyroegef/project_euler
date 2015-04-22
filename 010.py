import numpy as np

def isPrime(num):
	if num == 2:
		return True
	max_val = int(np.ceil(np.sqrt(num))+1)
	for x in range(2,max_val):
		if num%x == 0:
			return False
	return True

def sumPrimes(limit=2*10**6):
	output = 2
	test_val = 3
	while test_val < limit:
		if isPrime(test_val):
			output += test_val
		test_val += 2
	return output