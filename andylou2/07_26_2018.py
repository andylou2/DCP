# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class node():
	def __init__(self, val, next, visited=False):
		self.val = val
		self.next = next
		self.visited = visited


def findIntersection(root1, root2):
	curr1 = root1
	while curr1 != None:
		curr1.visited = True
		curr1 = curr1.next

	curr2 = root2
	while curr2 != None:
		if curr2.visited:
			return curr2.val
		else:
			curr2 = curr2.next

	return "No intersection found"

def main():
	tail = node(2, None)
	inter = node(5, tail)
	n1h = node(1, inter)
	n2h = node(3, inter)
	i = findIntersection(n1h, n2h)
	print(i)

if __name__ == '__main__':
	main()