# This problem was asked by Facebook.

# Given a function f, and N return a debounced f of N milliseconds.

# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

import signal
import time

def f():
	print("calling f")


def handler(*args):
	print("this is the handler")
	f()


def debounced_f(f, N):
	print("debouced_f")
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(N)
	print("alarm set")

if __name__ == '__main__':
	debounced_f(f, 5)
	for i in range(100):
		print(i)
		time.sleep(1)
		if i == 2:
			debounced_f(f, 5)