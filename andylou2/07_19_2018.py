# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longestDistinct(s, k):
	dict = {}
	numDist = 0
	maxLen = 0
	left = 0
	right = 0
	maxStr = ""			
	for c in s:
		dict[c] = 0

	for c in s:
		if dict[c] == 0:
			while numDist >= k:
				dict[s[left]] -=1
				if dict[s[left]] == 0:
					numDist -=1
				left += 1
			numDist += 1

		dict[c] += 1
		right += 1
		maxStr = s[left:right] if right-left > maxLen else maxStr
		maxLen = right - left if right-left > maxLen else maxLen
	return maxLen, maxStr


def main():
	k = 2
	s = "aaabcba"
	l, subString = longestDistinct(s, k)
	print(l, subString)

if __name__ == '__main__':
	main()