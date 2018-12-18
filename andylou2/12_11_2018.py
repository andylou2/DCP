# This problem was asked by Amazon.

# Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

def isPalindrome(s):
	dict = {}
	for c in s:
		if c in dict:
			dict[c] += 1
		else:
			dict[c] = 1

	return sum((dict[k]%2) for k in dict) == len(s) % 2


def main():
	s = "abcdeiiedcba"
	print(isPalindrome(s))

if __name__ == '__main__':
	main()