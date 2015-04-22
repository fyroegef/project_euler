import numpy as np

def isPrime(num):
	if num == 2:
		return True
	max_val = int(np.ceil(np.sqrt(num))+1)
	for x in range(2,max_val):
		if num%x == 0:
			return False
	return True

def prmFact(original_number):
	if isPrime(original_number):
		return [original_number]
	number = original_number
	output = []
	min_val = 2
	max_val = original_number
	while np.product(output) < original_number:
		for x in range(min_val,max_val+1):
			if number%x == 0:
				min_val = max(2,min_val-1)
				output.append(x)
				number = number/x
				max_val = number
				break
	if np.product(output) == original_number:
		return output

def smlMult(seq=range(2,21)):
	prime_factors = {}
	for x in seq:
		facts = prmFact(x)
		pfs = {}
		for f in facts:
			if not f in pfs:
				pfs[f] = 0
			pfs[f] += 1
		for f in pfs.keys():
			if not f in prime_factors:
				prime_factors[f] = 0
			prime_factors[f] = max(prime_factors[f],pfs[f])
	return np.product([f**prime_factors[f] for f in prime_factors.keys()])