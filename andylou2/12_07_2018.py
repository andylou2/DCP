# Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

# For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.


# def findMinDistance(s0, s1, sentence):
# 	toks = sentence.split(" ")
# 	print(toks)
# 	check = [s0, s1]
# 	flag = 2
# 	minDist = len(toks)
# 	dist = 0
# 	for s in toks:
# 		if flag == 2:
# 			if s == s0:
# 				flag = 1
# 			elif s == s1:
# 				flag = 0
# 		else:
# 			dist += 1
# 			if s == check[flag]:
# 				if dist < minDist:
# 					minDist = dist
# 					dist = 0
# 					if s == s0:
# 						flag = 1
# 					elif s == s1:
# 						flag = 0
# 			elif s == check[(1+flag)%2]: # this transforms 0 into 1 and 1 into 0... probably a better way to do this..
# 				dist = 0
# 	print(minDist)
# 	return minDist


def findMinDistance(s0, s1, sentence):
	toks = sentence.split(" ")
	print(toks)
	check = (s0, s1)
	minDist = len(toks)
	dist = 0

	for i, s in enumerate(toks):
		if s == check[True]:



# def findMinDistance(s0, s1, sentence):
# 	toks = sentence.split(" ")
# 	print(toks)
# 	check = [s0, s1]
# 	flag = 2
# 	minDist = 999999999
# 	dist = 0
# 	left = 0
# 	right = 0
# 	i = 0
# 	for s in toks:
# 		if flag == 2:
# 			if s == s0:
# 				flag = 1
# 				# left = i
# 			elif s == s1:
# 				flag = 0
# 				# left = i
# 		else:
# 			dist += 1
# 			if s == check[flag]:
# 				if dist < minDist:
# 					minDist = dist
# 					# right = i
# 			elif s == check[(1+flag)%2]:
# 				# left = i
# 				dist = 0
# 		i+=1
# 	print(minDist, left, right)
# 	return minDist


def main():
	s = "hello cat dog world hello"
	findMinDistance("hello", "world", s)

if __name__ == '__main__':
	main()