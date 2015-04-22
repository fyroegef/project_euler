import numpy as np

def multSum(ceiling=1000,divisors=[3,5]):
	output = 0
	for x in range(ceiling):
		if np.any([x%d == 0 for d in divisors]):
			output += x
	return output