def sumSq(limit=10):
	return sum(x**2 for x in range(1,limit+1))

def sqSum(limit=10):
	return sum(range(1,limit+1))**2

def sqsdiff(limit=10):
	return sqSum(limit=limit)-sumSq(limit=limit)

def altsqsdiff(limit=10):
	return sum((x-1)*x**2 for x in range(2,limit+1))