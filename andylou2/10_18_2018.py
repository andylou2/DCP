


class Node():
	def __init__(self, val, next):
		self.val = val
		self.next = next


def find_length(head):
	curr = head
	l = 0
	while curr != None:
		l += 1
		curr = curr.next
	return l

def print_list(head):
	curr = head
	while curr != None:
		print(curr.val, end='')
		print("->", end='')
		curr = curr.next
	print("None")
	return

def is_Palindrome(head):
	curr = head
	l = find_length(curr)

	for i in range(int(l/2)):
		curr = curr.next

	print_list(head)
	next = curr.next
	curr.next = None
	while next != None:
		nn = next.next
		next.next = curr
		curr = next
		next = nn
	print_list(head)
	print_list(curr)

def main():
	tail = Node(1, None)
	n5 = Node(3, tail)
	n4 = Node(4, n5)
	n3 = Node(4, n4)
	n2 = Node(3, n3)
	head = Node(1, n2)

	print(is_Palindrome(head))

if __name__ == '__main__':
	main()