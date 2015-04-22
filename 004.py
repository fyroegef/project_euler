import numpy as np

def isPalendrome(number):
	n = str(number)
	if np.all([n[m]==n[-1-m] for m in range(int(len(n)/2.))]):
		return True

def lrgPalendrome():
	dist = 0
	while True:
		for m in reversed(range(int(dist/2.))):
			n = (999-m)*(999-dist+m)
			if isPalendrome(n):
				return n
		dist += 1
