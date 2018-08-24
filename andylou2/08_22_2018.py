# This problem was asked by Facebook.

# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

def maxProfit(arr):
	mins = []
	diffs = []

	minimum = float("inf")
	for i in range(len(arr)):
		if arr[i] < minimum:
			minimum = arr[i]
			mins.append(minimum)
		d = arr[i] - min(mins)
		diffs.append(d)

	return max(diffs)



def main():
	arr = [9, 11, 8, 5, 7, 10, 20, 0, 16]
	m = maxProfit(arr)
	print("Maximum profit per share is: {}".format(m))

if __name__ == '__main__':
	main()