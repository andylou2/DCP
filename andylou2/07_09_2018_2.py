# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
def findSignChange(arr):
	found = False
	lower = 0
	upper = len(arr)
	i = len(arr) / 2
	if arr[-1] < 0:
		return len(arr) - 1
	if arr[0] >= 0:
		return 0
	while not found:
		if i > 0:
			if arr[i] >= 0 and arr[i-1] < 0:
				return i-1 if abs(arr[i]) > abs(arr[i-1]) else i
			elif arr[i] >= 0 and arr[i-1] >= 0:
				upper = i
				i = (lower + i) / 2
			else:
				lower = i
				i = (upper + i) / 2


def square(arr):
	i = findSignChange(arr)
	left = i - 1
	right = i + 1
	res = []
	res.append(arr[i]**2)
	for j in range(len(arr) - 1):
		# print("left: {}, right: {}".format(left, right))
		if left < 0:
			res.append(arr[right]**2)
			right += 1
		elif right >= len(arr):
			res.append(arr[left]**2)
			left -= 1
		else:
			if abs(arr[left]) < abs(arr[right]):
				res.append(arr[left]**2)
				left -= 1
			else:
				res.append(arr[right]**2)
				right += 1

	return res


def main():
	t = [-9, -2, 0, 2, 3]
	res = square(t)
	print(res)


if __name__ == '__main__':
	main()