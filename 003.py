import numpy as np

def isPrime(num):
	max_val = int(np.ceil(np.sqrt(num)))
	for x in range(2,max_val):
		if num%x == 0:
			return False
	return True

def largestPrimeFactor(number=600851475143):
	test_val = int(np.ceil(np.sqrt(number)))
	while True:
		if number%test_val == 0 and isPrime(test_val):
			if isPrime(number/test_val) and number/test_val > test_val:
				return number/test_val
			return test_val
		test_val -= 1