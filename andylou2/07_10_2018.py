# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def findMinMissing(arr):
	found = False
	for i in range(1,len(arr)):
		for j in range(len(arr)):
			if arr[j] == i:
				found = True
				break
		if not found:
			return i
		found = False


def findMinMissingFast(arr):
	max = 1
	for i in range(len(arr)):
		if arr[i] >= 0 and arr[i] <= max:
			max = arr[i] + 1
	return max


def main():
	# arr = [1,5,7,-1,2,4,5,5]
	# arr = [0]
	arr = [-1, 1,2,-3,4,5,8]

	m = findMinMissingFast(arr)
	print(arr)
	print("The first missing positive integer is: {}".format(m))


if __name__ == '__main__':
	main()