# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

def maxSubArray(arr):
	a = preprocess(arr)
	sum = 0
	sums = []
	for i in range(len(a)):
		if sum + a[i] > 0:
			sum += a[i]
		else:
			sums.append(sum)
	sums.append(sum)
	return max(sums)



def preprocess(arr):
	res = [arr[0]]
	sign = 1 if arr[0] > 0 else -1
	for i in range(1, len(arr)):
		if arr[i] > 0 and sign == 1:
			res[-1] += arr[i]
		elif arr[i] <= 0 and sign == -1:
			res[-1] += arr[i]
		else:
			res.append(arr[i])
		sign = 1 if arr[i] > 0 else -1
	return res

def main():
	arr = [34, -50, 42, 14, -1, -2, -10, -21, -5, 86, -120]

	s = maxSubArray(arr)
	print("the max subarray of {} is {}".format(arr, s))

if __name__ == '__main__':
	main()