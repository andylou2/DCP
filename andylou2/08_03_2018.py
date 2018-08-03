# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify(arr, k):
	currWord = arr[0]
	res = []
	for i in range(1, len(arr)):
		word = arr[i]
		if len(currWord) + len(word) > k:
			res.append(currWord)
			currWord = word
		else:
			currWord = currWord + " " + word

	res.append(currWord)
	res = padSpaces(res, k)
	return res

def padSpaces(arr, k):
	res = []
	for str in arr:
		toks = str.split(" ")
		diff = k - len(str)
		l = len(toks) - 1
		for i in range(len(toks) - 1):
			toks[i] = toks[i] + " "

		i = 0
		while diff > 0:
			i += 1
			toks[i % l] = toks[i % l] + " "
			diff -= 1
		i = 0
		res.append(''.join(toks))

	return res



def main():
	arr = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
	k = 16
	print(justify(arr, k))

if __name__ == '__main__':
	main()