# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

# 1	19
# 2	28
# 3	37
# 4	46
# 5	55
# 6	64
# 7	73
# 8	82
# 9	91
# 10	109
# 11	118
# 12	127
# 13	136
# 14	145
# 15	154
# 16	163
# 17	172
# 18	181
# 19	190
# 20	208
# 28	280
# 29	307
# 30	316

def getSum(n):
	s = str(n)
	res = reduce(lambda x, y : int(x) + int(y), s)
	return int(res)

def nPerfect(n):
	# return 19 + 9 * n
	i = 0
	counter = 0
	while i < n:
		while getSum(counter) != 10:
			counter += 1
		counter += 1
		i += 1
	return counter - 1


	# print(n)
	# if n < 10:
	# 	s = str(n)
	# 	inv = 10 - n
	# 	res = int(s + str(inv))
	# 	return res
	# else:
	# 	vals = 
	# 	print(str(n)[:-1])
	# 	return 

def main():
	for i in range(1, 20):
		print("the {}th perfect number is: {}".format(i, nPerfect(i)))

	print(nPerfect(29))

if __name__ == '__main__':
	main()