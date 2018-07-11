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

def swap(a, b):
	temp = a
	a = b
	b = a
	return

def findMinMissingFast(arr):
	i = 0
	while i < len(arr):
		# print(i, arr[i], arr[arr[i]-1], arr)
		if arr[i] > 0 and arr[i] < len(arr):
			temp = arr[i]
			arr[i], arr[temp-1] = arr[temp - 1], arr[i]
			if i > 0 and arr[i] > 0 and arr[i] - 1 < len(arr) and arr[i] != arr[arr[i]-1]:
				i-=1
			# i-=1
		i+=1


		# input[i] >= 0 and input[i] < len(input) and input[i] != i and input[input[i]] != input[i]:

	for i in range(len(arr)):
		if arr[i] != i + 1:
			return i + 1
	return len(arr) + 1


def main():
	# arr = [1,5,7,-1,2,4,5,5]
	# arr = [2, 1]
	# arr = [-1, 1,2,-3,4,5,8]
	# arr = [-10,-3,-100,-1000,-239,1]
	# arr = [1,2,3,4,5,6,7,8]
	# arr = [-1,4,2,1,9,10]
	# arr = [11,1,6,11,5,5,-6,9,-3,9,5,4,2,-8,16,-6,-4,2,3]
	# arr = [3,5,-3,-10,3,-4,9,7,-3,-1]
	# arr = [39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]
	arr = [-6,2,-9,5,3,12,-1,0,11,-4,18,1,-4,-8,9,-4,2,1,-6,1]

	print(arr)
	m = findMinMissingFast(arr)
	print(arr)
	print("The first missing positive integer is: {}".format(m))


if __name__ == '__main__':
	main()