from bisect import bisect_left
from more_itertools import peekable
x = [-7, -4,0]

def squaresort(input):
	i = bisect_left(input,0)
	pos = peekable(input[i:])
	neg = peekable(input[i-1::-1])
	output = []
	while pos or neg: 
		val, iter = min((pos.peek(float('inf')),pos), (-neg.peek(-float('inf')),neg), key=lambda x: x[0])
		output+= [val**2]
		iter.next()
	return output
	
print(squaresort(x))