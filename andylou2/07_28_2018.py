# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

def reOrder(arr, string):
	res = []
	iterCount = 0
	count = 0
	while len(arr) > 0 and count != len(string):
		s = arr.pop(0)
		l = len(s)
		if string[count:l+count] == s:
			res.append(s)
			count = count + l
			iterCount = 0
		else:
			arr.append(s)
			iterCount += 1
		if iterCount >= len(arr):
			return None

	return res


def main():
	arr = ['bed', 'bath', 'bedbath', 'and', 'beyond']
	# arr = ['hi', 'hello', 'haha']
	string = "bedbathandbeyond"
	print("The array: {}, reordered based on the string: {}".format(arr, string))
	nArr = reOrder(arr, string)
	print("results in: {}".format(nArr))
	

if __name__ == '__main__':
	main()