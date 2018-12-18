# This problem was asked by Google.

# Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

# If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

# Follow-up: If you can preprocess the array, can you do this in constant time?

def nearestLarger(arr, index):
	start = arr[index]
	min = 9999999 #np.inf
	mindex = None
	for i in range(1, len(arr)):
		right = index + i
		left = index - i
		if right < len(arr) and arr[right] > start and arr[right] < min:
			min = arr[right]
			mindex = right
		if left >= 0 and arr[left] > start and arr[left] < min:
		 	min = arr[left]
		 	mindex = left
	print("index: {}, value: {}".format(mindex, min))
	return min


def main():
	arr = [4, 1, 2, 6, 5]
	nearestLarger(arr, 0)

if __name__ == '__main__':
	main()