# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class node():
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

def numSubUnival(n):
	if n == None:
		return True, 0

	left, countLeft = numSubUnival(n.left)
	right, countRight = numSubUnival(n.right)
	# print("left: {}, right: {}, countLeft: {}, countRight: {}".format(left, right, countLeft, countRight))
	total = countLeft + countRight
	if not left:
		return False, total
	if not right:
		return False, total
	if n.left and n.left.val != n.val:
		return False, total
	if n.right and n.right.val != n.val:
		return False, total

	return True, total + 1
	# l = preOrder(n)
	# print(l)





def preOrder(n):
	if n.left == None and n.right == None:
		return [n.val]
	else:
		return [n.val] + preOrder(n.left) + preOrder(n.right)





def main():
	n1 = node(1, None, None)
	n2 = node(1, None, None)
	n3 = node(1, n1, n2)
	n4 = node(0, None, None)
	n5 = node(0, n3, n4)
	n6 = node(0, None, None)
	root = node(0, n6, n5)

	x, num = numSubUnival(root)
	print("The tree has {} unival subtrees".format(num))

if __name__ == '__main__':
	main()