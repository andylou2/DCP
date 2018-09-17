
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the head of a singly linked list, reverse it in-place.

# Upgrade to premium and get in-depth solutions to every problem.

class node:
	def __init__(self, next, val):
		self.next = next
		self.val = val

	def __str__(self):
		return val

def printLL(head):
	curr = head
	while curr != None:
		print curr.val
		curr = curr.next

def reverseInPlace(node):
	prev = None
	curr = node
	while curr != None:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next



def main():
	tail = node(None, 4)
	n2 = node(tail, 3)
	n1 = node(n2, 2)
	head = node(n1, 1)
	print("Before: ")
	printLL(head)
	reverseInPlace(head)
	print("After: ")
	printLL(tail)

if __name__ == '__main__':
	main()