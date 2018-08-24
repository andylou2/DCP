import pptree
class Node:
	def __init__(self, input):
		if isinstance(input, list):
			val, left, right = input
			self.val = val
			self.children = [Node(left),Node(right)]
		else:
			self.val = input
			self.children = []
	def print(self):
		pptree.print_tree(self, childattr='children', nameattr='val')
	def to_list(self):
		if self.children == []:
			return self.val
		return [self.val]+ list(map(lambda x: x.to_list(), self.children))
	def __str__(self):
		return str(self.to_list())
		
s = Node(['a',['b','e','f'],'c'])
t = Node(['b', 'd', 'e'])

s.print()
t.print()

print(str(s).find(str(t)))