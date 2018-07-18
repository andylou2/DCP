# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def countPermutationsFixed(n):
	if n == 1:
		return 1
	else:
		arr = [1, 1]
		for i in range(1,n):
			arr.append(arr[i] + arr[i-1])
		return arr[-1]

def countPermutations(n, steps):
	if n == 1:
		return 1
	else:
		arr = [1]
		for i in range(1,n):
			sum = 0
			for index in steps:
				if i - index < 0:
					sum += 0
				else:
					sum +=  arr[i - index]
			arr.append(sum)
		print(arr)
		return arr[-1]

def main():
	print(countPermutationsFixed(1))
	print(countPermutationsFixed(2))
	print(countPermutationsFixed(3))
	print(countPermutationsFixed(4))
	print(countPermutationsFixed(5))
	print(countPermutations(1, [1,2,3]))
	print(countPermutations(2, [1,2,3]))
	print(countPermutations(3, [1,2,3]))
	print(countPermutations(4, [1,2,3]))
	print(countPermutations(8, [1,2,3]))
	print(countPermutations(1, [1,3]))
	print(countPermutations(2, [1,3]))
	print(countPermutations(3, [1,3]))
	print(countPermutations(4, [1,3]))
	print(countPermutations(8, [1,3]))
	print(countPermutations(1, [1]))
	print(countPermutations(2, [1]))
	print(countPermutations(3, [1]))
	print(countPermutations(8, [1]))

if __name__ == '__main__':
	main()