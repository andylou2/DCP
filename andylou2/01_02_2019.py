# This problem was asked by Google.

# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

class node():
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

def levelOrder(root):
	queue = [root]
	while len(queue) > 0:
		curr = queue.pop(0)
		print(curr.val)
		if curr.left != None:
			queue.append(curr.left)
		if curr.right != None:
			queue.append(curr.right)
		


def buildTree(arr):
	print(arr)
	if len(arr) == 0:
		return None
	if len(arr) == 1:
		return node(arr[0], None, None)
	root = arr[-1]
	firstLarger = 0
	for i, val in enumerate(arr):
		if val > root:
			firstLarger = i
			break

	root_left = buildTree(arr[:firstLarger])
	root_right = buildTree(arr[firstLarger:-1])

	return node(root, root_left, root_right)

def main():
	postOrder = [2, 4, 3, 8, 7, 5]
	r = buildTree(postOrder)
	levelOrder(r)

if __name__ == '__main__':
	main()