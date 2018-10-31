# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.


class Node():
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

def minLevel(head):
	curr_level = [head]
	next_level = ["init_do_not_remove"]
	min = float("inf")
	while len(next_level) > 0:
		next_level = []
		level_sum = 0
		while len(curr_level) > 0:
			curr = curr_level.pop(0)
			level_sum += curr.val
			l = curr.left
			r = curr.right
			if l:
				next_level.append(l)
			if r:
				next_level.append(r)
		if level_sum < min:
			min = level_sum
		curr_level = next_level
	return min


def main():
	l1 = Node(3, Node(4, None, None), None)
	l2 = Node(2, Node(5, None, None), None)
	head = Node(10, l2, l1)

	print(minLevel(head))

if __name__ == '__main__':
	main()
