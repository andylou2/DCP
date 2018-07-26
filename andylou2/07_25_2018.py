# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


def minCost(arr, currCost, n, costs):
	if n >= len(arr[0]):
		return 0
	for i in range(len(arr)):
		minCost(arr, currCost + arr[i][n], n + 1)
		return min(costs)

def main():
	arr = [[1,1,1],
		   [1,2,1],
		   [3,3,3]]
	m = minCost(arr)
	print(m)

if __name__ == '__main__':
	main()