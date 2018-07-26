# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.


def getChildren(arr, index, level):
	children = []
	for i in range(index, len(arr)):
		if arr[i][:level] == '\t'*level:
			if arr[i][level:level+1] != '\t':
				children.append((i, arr[i]))
		else:
			break
	return children

# def findAllLeaves(arr):
# 	leaves = []
# 	for s in arr:
# 		if '.' in s:
# 			leaves.append(s)
# 	return leaves

def findLongestPath(sys):
	t = sys.split("\n")
	print(t)

	s = [(0,t[0])]
	visited = []
	maxPath= ""
	currPath = ""
	currLevel = 0
	prevLevel = -1

	while len(s) > 0:
		i, fil = s.pop()
		currLevel = fil.count('\t')
		print("curr is: {} with index: {}".format(fil, i))
		if fil not in visited:
			visited.append(fil)
			if currLevel > prevLevel:
				currPath = currPath + '/' + fil
				print("path: {}".format(currPath))
			if '.' not in fil:
				children = getChildren(t, i + 1, currLevel + 1)
				print("children of: {} are: {}".format(fil, children))
				for c in children:
					s.append(c)


		prevLevel = currLevel

			

	# path = ""
	# for i in range(len(t)):
	# 	fil = t[i]
	# 	curr_depth = getDepth(fil)
	# 	if curr_depth <= prev_depth:
	# 		max_path = max(, key=len)
	# 	else:
	# 		path = path + '/' + fil


	return 0

def main():
	# sys = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
	sys = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
	s = findLongestPath(sys)
	print("the longest path is: {}".format(s))

if __name__ == '__main__':
	main()