# This problem was asked by Amazon.

# Given a node in a binary tree, return the next bigger element, also known as the inorder successor.

# For example, the inorder successor of 22 is 30.

#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.


class Node():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	# def insert()

def main():
	n2 = Node(2)
	i = 1
	n = Node(1, n2)

	print(id(n2))
	print(id(n))
	print(id(i))

if __name__ == '__main__':
	main()