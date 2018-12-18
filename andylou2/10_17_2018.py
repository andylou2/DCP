# This problem was asked by Square.

# Given a string and a set of characters, return the shortest substring containing all the characters in the set.

# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

# If there is no substring containing all the characters in the set, return null.

recursive strategy:

def substring(i, j, s, set)
if len(s[i:j]) < len(set):
	return np.inf
if s[i:j] satisfies set:
	return min(len(s[i:j], substring[i+1, j+1]))
else:
	return min(substring[i+1, j], substring[i, j+1])

# If the set doesn't contain every letter, add the letter to the right. While the set contains all letters, remove letters from the left.

figehaeciaei


aeciaeciaeciaeciaeciaei