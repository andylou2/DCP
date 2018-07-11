def cons(a,b):
	def pair(f):
		return f(a,b)
	return pair

def cdr(pair):
	return pair(lambda x,y: y)
	
print(cdr(cons(3,4)))