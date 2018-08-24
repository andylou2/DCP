def reconstruct(string, dict):
	stack = []
	index = 0
	offset = 1
	while index != len(string):
		for i in range(index+offset, len(string)+1):
			print("Checking {0}".format(string[index:i]))
			if string[index:i] in dict:
				print("Match found! Pushing {0}".format(string[index:i]))
				stack.append((string[index:i],index))
				index = i
				offset = 1
				break
		else:	
			if stack:
				
				word, index = stack.pop()
				print("Popping {0}".format(word))
				offset = len(word)+1
			else:
				return None
	return [word[0] for word in stack]
	
dict = {"bed","bath","bedbathand","beyond"}
string = "bedbathandbeyond"

print(reconstruct(string,dict))