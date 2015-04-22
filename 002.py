def sumEven(seq=[1,2],ceiling=4*10**6):
	output = 2
	# add = False
	while True:
		seq = [seq[1],sum(seq)]
		# if add:
		if seq[1]%2 == 0:
			if seq[1] > ceiling:
				return output
			output += seq[1]
			# add = False
		# else:
		# 	add = True

## NB: was first summing terms with an even index rather than those divisible by 2, left answer because interesting

## also of interest on checking the answer is that even Fib terms obey the relation:
## E(n) = 4*E(n-1) + E(n-2)  where if E(n) = F(n) then E(n-1) = F(n-3), etc.