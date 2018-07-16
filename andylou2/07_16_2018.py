# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import threading
import time
import signal

def fWrapper(n):
	time.sleep(n/1000.0)
	print("slept for {} miliseconds".format(n))
	f()
	return 

def f():
	print("running f!")
	return


def main():
	n = 100
	t = threading.Thread(target=fWrapper, args=(n,))
	t.start()
	print("main thread chugging along")
	t.join()

if __name__ == '__main__':
	main()