# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def findPrefix(prefix, arr):
	l = len(prefix)
	res =[]

	for ele in arr:
		if ele[:l] == prefix:
			res.append(ele)
		if ele[:l] > prefix:
			break
	return res

def findPrefixFast(prefix, arr):
	if arr == []:
		return
	l = len(prefix)
	res = []

	lo = 0
	hi = len(arr) - 1
	start = int((lo + hi) / 2)
	while True:
		ele = arr[start]
		if ele[:l] == prefix:
			break
		elif ele[:l] < prefix:
			start = int((lo + start) / 2)
		else:
			start = int((start + hi) / 2)

	for i in range(start, len(arr)):
		if arr[i][:l] == prefix:
			res.append(arr[i])
		if ele[:l] > prefix:
			break

	for i in range(start - 1, -1, -1):
		if arr[i][:l] == prefix:
			res.append(arr[i])
		if ele[:l] < prefix:
			break
	return res


def main():
	arr = ["dog", "deer", "deal"]
	prefix = "de"
	print(findPrefixFast(prefix, sorted(arr)))

if __name__ == '__main__':
	main()