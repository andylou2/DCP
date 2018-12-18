# This problem was asked by Jane Street.

# Generate a finite, but an arbitrarily large binary tree quickly in O(1).

# That is, generate() should return a tree whose size is unbounded but finite.
import math
class Node():
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		queue = [self]
		numNodes = 0
		while len(queue) > 0:
			numNodes += 1
			curr = queue.pop()
			l = curr.left
			r = curr.right
			if l != None:
				queue.append(l)
			if r != None:
				queue.append(r)
		print(numNodes)

		current_level = [self]
		while current_level:
			offset = ' ' * numNodes
			numNodes = int(math.ceil((numNodes - 1)/ 2.0))
			s = ""
			for node in current_level:
				if node == '\t':
					s = s + offset
				else:
					s = s + offset + node.val
			print(s)
			next_level = []
			for n in current_level:
				if n != '\t':
					if n.left:
						next_level.append(n.left)
					else:
						next_level.append('\t')
					if n.right:
						next_level.append(n.right)
					else:
						next_level.append('\t')
			current_level = next_level
		return ""

def main():
	l1 = Node('c', Node('d', None, None), None)
	l2 = Node('b', Node('e', None, None), None)
	head = Node('a', l2, l1)

	print(head)

if __name__ == '__main__':
	main()