# This problem was asked by Google.
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
# A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

import math

class node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def toList(self):
		res = []
		s = [self]
		while len(s) > 0:
			curr = s.pop(0)
			if curr == None:
				res.append("*")
			else:
				res.append(curr.value)
				s.append(curr.left)
				s.append(curr.right)
		self.height = int(math.log(len(res), 2))
		res = res[:2**self.height - 1]
		self.res = res
		return res

	# def __str__(self):
	# 	h = self.height
	# 	print(h)
	# 	res = ""
	# 	for i in range(len(self.res)):
	# 		level = math.log(i + 2, 2)
	# 		print(level)
	# 		res += (" " * (h - math.ceiling(level))) + self.res[i]
	# 		if level.is_integer() and level:
	# 			res += "\n"

	# 	return res



def preOrder(root):
	res = []
	s = [root]
	while len(s) > 0:
		curr = s.pop()
		res.append(curr.value)
		if curr.left == None and curr.right != None:
			s.append(curr.right)
		elif curr.left != None and curr.right == None:
			s.append(curr.left)
		elif curr.left != None and curr.right != None:
			s.append(curr.right)
			s.append(curr.left)

	return res

def levelOrder(root):
	res = []
	s = [root]
	while len(s) > 0:
		curr = s.pop(0)
		res.append(curr.value)
		if curr.left == None and curr.right != None:
			s.append(curr.right)
		elif curr.left != None and curr.right == None:
			s.append(curr.left)
		elif curr.left != None and curr.right != None:
			s.append(curr.left)
			s.append(curr.right)
			

	return res

def inOrder(curr, res):
	if curr == None:
		return
	inOrder(curr.left, res)
	res.append(curr.value)
	inOrder(curr.right, res)

def postOrder(curr, res):
	if curr == None:
		return
	postOrder(curr.left, res)
	postOrder(curr.right, res)
	res.append(curr.value)


def findSubtree(S, W):
	preOrderS = preOrder(S)
	preOrderW = preOrder(W)
	inOrderS = []
	inOrder(S, inOrderS)
	inOrderW = []
	inOrder(W, inOrderW)

	preSub = subListBrute(preOrderS, preOrderW)
	inSub = subListBrute(inOrderS, inOrderW)

	if preSub == True and inSub == True:
		return True
	else:
		return False

def subListBrute(S, W):
	for j in range(len(S)):
		for i in range(len(W)):
			# print("matching S[j] = {} with W[i] = {} at location j={} and i={}".format(S[j], W[i], j, i))
			if S[j] != W[i]:
				break
			else:
				j+=1
			if i == len(W) - 1:
				return True
	return False

def subList(S, W):
	T = preProcess(W)
	j = 0
	for i in range(len(S)):
		if S[i] == W[j]:
			j+=1
			if j == len(W):
				return true
		else:
			j = T[j]
			if j < 0:
				j+=1
				i+=1
	return false

	
def preProcess(W):
	T = [-1]
	j = 0
	for i in range(1, len(W)):
		if W[i] == W[j]:
			T.append(T[j])
			j+=1
		else:
			T.append(j)
			j = T[j]
			while j >= 0 and W[i] != W[j]:
				j = T[j]
			j += 1
		# print("W[j]: {}, W[i]:{}, i:{}, j: {}".format(W[j], W[i], i, j))
	return T


def main():
	# root
	#     a
	#    / \
	#   b   c
	#  /
	# d
	root = node('a')
	root.left = node('b')
	root.right = node('c')
	root.left.left = node('d')

	# root2
	#   b
	#  /
	# d
	root2 = node('b')
	root2.left = node('d')

	# root3
	#     a
	#    / \
	#   b   c
	#  /     \
	# d       e
	root3 = node('a')
	root3.left = node('b')
	root3.right = node('c')
	root3.right.right = node('e')
	root3.left.left = node('d')

	# root4
	#   b
	#  / \
	# d   e
	root4 = node('c')
	# root4.left = node('d')
	root4.right = node('e')

	preRes = preOrder(root)
	print("PreOrder: {}".format(preRes))

	inRes = []
	inOrder(root, inRes)
	print("InOrder: {}".format(inRes))

	postRes = []
	postOrder(root, postRes)
	print("PostOrder: {}".format(postRes))

	levelRes = levelOrder(root)
	print("LevelOrder: {}".format(levelRes))

	res = findSubtree(root, root2)
	print("root2 is a subtree of root: {}".format(res))

	res2 = findSubtree(root3, root4)
	print("root4 is a subtree of root2: {}".format(res2))

	# lis = root3.toList()
	# print(lis)
	# print(root3)

if __name__ == '__main__':
	main()