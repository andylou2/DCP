# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
	res = []
	q = [root]
	while len(q) > 0:
		curr = q.pop(0)
		if curr == None:
			res.append("*")
		else:
			q.append(curr.left)
			q.append(curr.right)
			res.append(curr.val)

	# s = ""
	# for ele in res:
	# 	s += str(ele)
	# 	s += ","
	# print(s[:-1])
	# return s[:-1]
	return res


def deserialize(s, num):
	# print("s: {}, num: {}".format(s, num))
	if num+1 >= len(s):
		return
	if s[num-1] == "*":
		return
	l = 2*num
	r = 2*num + 1
	return Node(s[num-1], deserialize(s, l), deserialize(s, r))


def main():
	n4 = Node(4)
	n3 = Node(3, n4)
	n2 = Node(2)
	n = Node(1, n2, n3)
	arr = serialize(n)
	newn = deserialize(arr, 1)
	temp = serialize(newn)
	print(temp)

	node = Node('root', Node('left', Node('left.left')), Node('right'))
	assert deserialize(serialize(node),1).left.left.val == 'left.left'

if __name__ == '__main__':
	main()