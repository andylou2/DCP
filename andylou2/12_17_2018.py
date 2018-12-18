# This problem was asked by Jane Street.

# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.


def evaluateReversePolish(arr):
	s = []

	for ele in arr:
		if isinstance(ele, int):
			s.append(ele)
		else:
			ele1 = str(s.pop())
			ele2 = str(s.pop())
			s.append(eval(ele2 + ele + ele1))
		print(s)
	return s.pop()

def main():
	# arr = [5, 3, '+']
	arr = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
	x = evaluateReversePolish(arr)
	print(x)

if __name__ == '__main__':
	main()