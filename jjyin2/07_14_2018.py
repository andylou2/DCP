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
	def is_unival(self):
		if self.val == '': 				#placeholder empty node
			return '', True, 0			
		if self.children == []:
			return self.val, True, 1
		left_val,  left_unival,  left_count = self.children[0].is_unival()
		right_val, right_unival, right_count = self.children[1].is_unival()
		
		equal_or_leaf = lambda x, y: x=='' or y=='' or x==y
		same_val =  equal_or_leaf(self.val,left_val) \
				and equal_or_leaf(self.val,right_val)
		is_unival = left_unival and right_unival and same_val

		return self.val, is_unival, left_count+right_count+(1 if is_unival else 0)
	
s = Node(['0','1',['2',['2','2','2'],'2']])
s.print()
_, _, count = s.is_unival()
print(count)
#t = Node(['b', 'd', 'e'])


#t.print()

#print(str(s).find(str(t)))