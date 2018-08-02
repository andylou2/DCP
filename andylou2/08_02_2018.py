# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def dfs(s):
	stack = []

	for c in s:
		if c == '(' or c == '[' or c == '{':
			stack.append(c)
		else:
			last = stack.pop()
			if c == ')':
				if last != '(':
					return False
			if c == ']':
				if last != '[':
					return False
			if c == '}':
				if last != '{':
					return False
		
	if len(stack) > 0:
		return False
	return True



def main():
	s = "((()"
	s = "([)"
	s = "([])[]({})"
	if dfs(s):
		print("{} is a balanced string".format(s))
	else:
		print("{} is not a balanced string".format(s))

if __name__ == '__main__':
	main()