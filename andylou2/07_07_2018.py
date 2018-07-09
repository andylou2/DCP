
# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def twoSum(arr, target):
	h = {}
	for i in range(len(arr)):
		val = arr[i]
		print(val)
		print(h)
		if val not in h.keys():
			h[target - val] = (val, i)
		else:
			return True, i, h[val][1]
	return False


def main():
	print(twoSum([1,2,3,4,5,6], 10))


if __name__ == '__main__':
	main()