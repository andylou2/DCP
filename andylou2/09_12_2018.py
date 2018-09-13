
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

# For example, given M = 5 and the list of bishops:

# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
# The board would look like this:

# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
def nCr(n, r):
	numerator = reduce(lambda x, y : x * y, range(n - r + 1, n + 1))
	denominator = reduce(lambda x, y : x * y, range(1, r + 1))
	res = numerator / (denominator + 0.0)
	return res


def numAttacks(arr, M):
	bishops = {}
	for loc in arr:
		bishops[loc] = False
	totalPairs = 0
	for loc in arr:
		if bishops[loc] == True:
			pass
		else:
			numBishop = getBishopsDiag(loc, bishops, M)
			numPairs = nCr(numBishop, 2)
			totalPairs += numPairs
	return int(totalPairs)

def getBishopsDiag(loc, bishops, M):
	x = loc[0]
	y = loc[1]

	numBishop = 1
	while x < M and y < M:
		x += 1
		y += 1
		curr = (x,y)
		if curr in bishops:
			bishops[curr] = True
			numBishop += 1

	x = loc[0]
	y = loc[1]
	while x >= 0 and y >= 0:
		x -= 1
		y -= 1
		curr = (x,y)
		if curr in bishops:
			bishops[curr] = True
			numBishop += 1

	x = loc[0]
	y = loc[1]
	while x < M and y >= 0:
		x += 1
		y -= 1
		curr = (x,y)
		if curr in bishops:
			bishops[curr] = True
			numBishop += 1

	x = loc[0]
	y = loc[1]
	while x >= 0 and y < M:
		x -= 1
		y += 1
		curr = (x,y)
		if curr in bishops:
			bishops[curr] = True
			numBishop += 1
	return numBishop

def main():
	arr = [(0, 0), (1, 2), (2, 2), (4, 0), (1, 1)]
	arr = [(0, 0), (1, 1), (2, 0), (0,2)]
	M = 5
	print(numAttacks(arr, M))

if __name__ == '__main__':
	main()