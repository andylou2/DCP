# This question was asked by Google.

# Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
# Return 4.

def maxRect(arr):
	for i in range(len(arr)):
		line = ""
		for j in range(len(arr[0])):
			line += str(arr[i][j]) + " "
		print(line)

	for 


def main():

	arr = [[1, 0, 0, 0], 
		   [1, 0, 1, 1], 
		   [1, 0, 1, 1], 
		   [0, 1, 0, 0]]

	print(arr)

	maxRect(arr)
if __name__ == '__main__':
	main()