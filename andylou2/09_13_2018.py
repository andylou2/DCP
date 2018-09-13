
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.
def largestProd(arr):
	arr = sorted(arr)

	neg1 = arr[0]
	neg2 = arr[1]

	pos1 = arr[-1]
	pos2 = arr[-2]
	pos3 = arr[-3]

	max1 = neg1 * neg2 * pos1
	max2 = pos1 * pos2 * pos3
	print(max1, max2)
	return max(max1, max2)

def main():
	arr = [-10, -10, -9, 5, 2, 10, 11, 6, 11]
	print(largestProd(arr))

if __name__ == '__main__':
	main()