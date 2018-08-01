# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

class node():
	def __init__(self, val, next):
		self.val = val
		self.next = next


def kthLast(root, k):
	pt1 = root
	for i in range(k):
		pt1 = pt1.next
	pt2 = root
	while pt1.next != None:
		pt1 = pt1.next
		pt2 = pt2.next

	return pt2.val

def main():
	root = node(1, node(2, node(3, node(4, node(5, node(6, None))))))

	k = 3
	v = kthLast(root, k)
	print("The {} to last node has val: {}".format(k, v))

if __name__ == '__main__':
	main()