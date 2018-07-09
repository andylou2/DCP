
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# Upgrade to premium and get in-depth solutions to every problem.

# If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
def findExclusiveMemo(arr):
	memBackward = []
	memForward = []

	memBackward.append(arr[-1])
	memForward.append(arr[0])

	size = len(arr)
	for i in range(1, size):
		memBackward.append(memBackward[i-1] * arr[size - i - 1])
		memForward.append(memForward[i-1] * arr[i])
	# print("Backwards: {}".format(memBackward))
	# print("Forward: {}".format(memForward))
	# print("Original: {}".format(arr))
	arr[0] = memBackward[-2]
	arr[-1] = memForward[-2]
	for i in range(1, size - 1):
		# print("i: {}, size - i - 2: {}, backward: {}, foreward: {}".format(i, size - i - 2, memBackward[size - i - 2], memForward[i - 1]))
		arr[i] = memBackward[size - i - 2] * memForward[i - 1]
	return arr

def findExclusive(arr):
	mult = reduce (lambda x, y: x * y, arr)
	return [mult/ele for ele in arr]

def main():
	arr = [2,5,7, 10, 3]
	res = findExclusive(arr)
	res2 = findExclusiveMemo(arr)
	print(res)
	print(res2)
	assert res == res2


if __name__ == '__main__':
	main()