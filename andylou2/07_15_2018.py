# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?
import copy

def maxNonadjacent(arr):
	if len(arr) == 0:
		return 0
	elif len(arr) == 1:
		return arr[0]
	val = arr[0]

	# print(val, arr)
	return max(val + maxNonadjacent(copy.deepcopy(arr[2:])), maxNonadjacent(copy.deepcopy(arr[1:])))

def maxNonadjacentFast(arr):
	maxWith = 0
	maxWithout = 0

	for ele in arr:
		maxCurr = max(maxWith, maxWithout)
		maxWith = maxWithout + ele
		maxWithout = maxCurr

	return max(maxWith, maxWithout)


def main():
	arr = [2,4,6,2,5]
	# arr = [5,1,1,5]
	m = maxNonadjacent(arr)
	print(m)

if __name__ == '__main__':
	main()