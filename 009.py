import numpy as np

def specPythTrip(spec_sum=1000):
	for c in reversed(range(333,1000)):
		for b in range(int(np.floor((1000-c)/2.)),1000-c):
			a = 1000 - b - c
			if a**2 + b**2 == c**2:
				print a,b,c
				return a*b*c