# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def countDecodes(s):
	#This does not work..
	l = len(s)
	if l < 2:
		return l

	firstTwo = int(s[0:2])

	if l == 2:
		if firstTwo <= 26:
			return 2
		else:
			return 1

	if firstTwo <= 26:
		return 2 * countDecodes(s[2:]) + countDecodes(s[1:]) - 1
	else:
		return countDecodes(s[1:])


def countDecodesFast(s):
	l = len(s)
	if l < 2:
		return l

	arr = [1]
	firstTwo = s[0:2]
	if int(firstTwo) <= 26:
		arr.append(2)
	else:
		arr.append(1)
	for i in range(1,l-1):
		firstTwo = s[i:i+2]
		# print("firsttwo: {}".format(firstTwo))
		if int(firstTwo) <= 26:
			arr.append(arr[i-1] + arr[i])
		else:
			arr.append(arr[i])
		# if arr[i-2:i]:

	print("num: {}".format(arr[-1]))
	return arr[-1]

def main():
	s = '11111'
	c = countDecodes(s)
	print(c)

	c2 = countDecodesFast(s)
	print(c2)

if __name__ == '__main__':
	main()