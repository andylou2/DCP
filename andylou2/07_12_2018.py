# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
import _ctypes

class node():
	def __init__(self, val, prev=None, next=None):
		self.val = val
		if prev == None and next == None:
			self.both = None
		elif prev == None:
			self.both = hex(id(next))
		elif next == None:
			self.both = hex(id(prev))
		else:	 
			self.both = hex(id(prev) ^ id(next))
		# print(self.both)


class linkedlist():
	def __init__(self, root):
		self.root = root
		self.end = root

	def add(self, val):
		print("before, root: {}, end: {}".format(hex(id(self.root)), hex(id(self.end))))
		print("adding: {}".format(val))
		n = node(val, hex(id(self.end)), None)
		print("CREATING NODE AT: {} WITH VALUE: {}".format(hex(id(n)), val))
		print("value:{}".format(n.val))
		prev = self.end.both
		if prev == None:
			self.end.both = hex(id(n))
		else:
			self.end.both = hex(id(n) ^ int(prev, base=16))
		self.end = n
		print("after, root: {}, end: {}, value:{}".format(hex(id(self.root)), hex(id(self.end)), self.end.val))

	def get(self, index):
		i = 0
		while i < index:
			if prev == None:
				next = _ctypes.PyObj_FromPtr(int(curr.both, base=16))
				assert type(next) == node
				print("next is type node: with value: {}".format(node.val))
			else:
				next = _ctypes.PyObj_FromPtr(int(curr.both, base=16) ^ id(prev))
				assert type(next) == node
				print("next is type node: with value: {}".format(node.val))
			prev = curr
			curr = next
		return curr

	def pri(self):
		curr = self.root
		prev = None
		while curr != self.end:
			print(curr.val)
			print(curr.val, hex(id(curr)), curr.both, prev, hex(id(prev)))
			if prev == None:
				next = _ctypes.PyObj_FromPtr(int(curr.both, base=16))
				assert type(next) == node
				print("next is type node: with value: {}".format(node.val))
			else:
				next = _ctypes.PyObj_FromPtr(int(curr.both, base=16) ^ id(prev))
				assert type(next) == node
				print("next is type node: with value: {}".format(node.val))
			prev = curr
			curr = next
			print(hex(id(curr)))
			# , curr.both, prev, hex(id(prev)))

def main():
	ll = linkedlist(node(0))
	ll.add(1)
	ll.add(3)
	ll.pri()


if __name__ == '__main__':
	main()