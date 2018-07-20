# This problem was asked by Google.

# The area of a circle is defined as pir^2. Estimate pi to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def montecarlo(n, m):
	s = 0.0
	n2 = n**2
	for i in range(m):
		x = random.uniform(-n, n)
		y = random.uniform(-n, n)
		if x**2 + y**2 <= n2:
			s += 1
	percent = s/m
	area = percent * (n*2)**2
	return area/(n2)


def main():
	p = montecarlo(1, 500000)
	print(p)


if __name__ == '__main__':
	main()