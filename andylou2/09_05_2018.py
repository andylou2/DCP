# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

def naive_pow(a, b):
	prod = a
	for i in range(b - 1):
		prod = a * prod
	return prod

def pow(a, b):
	prod = a
	offset = 1
	while b > 1:
		print("reducing to {}^{} * {}".format(prod, b, offset))
		offset = offset * prod if b%2 == 1 else offset
		b = b >> 1
		prod = prod * prod
	prod = prod * offset

	return prod

def main():

	a = 14
	b = 14
	# for i in range(a):
	# 	for j in range(b):
	# 		naive = naive_pow(i, j)
	# 		fast = pow(i, j)
	# 		assert naive == fast
	naive = naive_pow(a, b)
	fast = pow(a, b)
	print("naive: {}, fast: {}".format(naive, fast))


if __name__ == '__main__':
	main()