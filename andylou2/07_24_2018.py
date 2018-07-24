# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

def maxSubarray(arr, k):
	print("Finding max of subarrays of size: {} from: {}".format(k, arr))
	if len(arr) <= k:
		print(max(arr))
		return
	subArr = arr[:k]
	print("Subarray: {} has max: {}".format(subArr, max(subArr)))
	for i in range(k, len(arr)):
		subArr[i%k] = arr[i]
		print("Subarray: {} has max: {}".format(subArr, max(subArr)))


def main():
	arr = [10, 5, 2, 7, 8, 7]
	k = 3
	maxSubarray(arr, k)

if __name__ == '__main__':
	main()