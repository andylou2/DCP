# What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
import copy

def makefunc(i):
	return lambda : i
functions = []
for i in range(10):
	functions.append(makefunc(i))

for f in functions:
	print(f())