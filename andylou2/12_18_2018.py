# This problem was asked by Google.

# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

def findDupe(arr):
	# s = sum(arr)
	# n = len(arr)
	# base = n*(n-1) / 2
	# diff = s - base
	# print(diff)
	for i in range(len(arr)):
		if arr[abs(arr[i])] < 0:
			return abs(arr[i])
		else:
			arr[abs(arr[i])] *= -1


def main():
	arr = [7,6,5,4,3,2,2,7]
	index = findDupe(arr)
	print("the dupe is: {}".format(index))

if __name__ == '__main__':
	main()



# [1,2,1]
# Read index 0: 1
# Check index abs(1): 2>0
# True, so negate.
# [1,-2,1]
# Read index 1: -2
# Check index abs(-2): 1>0
# True, so negate 
# [1,-2,-1]
# Read index 2: -1
# Check index abs(-1): -1>0
# False. Return abs(-1)