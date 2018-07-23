# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
import random

def rand_stream():
	num = 0
	count = 0
	while True:
		i = raw_input()
		if str(i) == 'q':
			break
		i = int(i)
		if count == 0:
			num = i
		else:
			r = random.randint(0, count)
			if r == count:
				num = i
		count += 1
	print("your number was: {}".format(num))

def main():
	rand_stream()

if __name__ == '__main__':
	main()

