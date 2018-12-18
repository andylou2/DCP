# This problem was asked by Google.

# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

def find_indicies(c1, s2):
	res = []
	for i in range(len(s2)):
		if c1 == s2[i]:
			res.append(i)
	return res

def isShifted(s1, s2):
	if len(s1) != len(s2):
		return False
	res = find_indicies(s1[0], s2)
	# print(res)

	counter = 0
	for index in res:
		flag = True
		for i in range(1, len(s1)):
			counter+=1
			if s1[i] != s2[(i+index)%len(s1)]:
				flag = False
				break
		if flag == True:
			return True, counter + len(index)
	return False, counter + len(index)

def main():
	s1 = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"
	s2 = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010100"
	print(isShifted(s1, s2))

if __name__ == '__main__':
	main()