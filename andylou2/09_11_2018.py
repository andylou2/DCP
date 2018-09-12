# This problem was asked by Google.

# Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

cache_values = {}
cache = []
cache_size = 3

def get(key):

def set(key, value):
	if len(cache_values) >= cache_size:
		#todo
	else:
		if key not in cache_values:
			cache_values[key] = (0, value)
			if len(cache) > 0:
				if cache_values[cache[-1][0]][0] == 0:
					cache[-1].append(key)
				else:
					cache.append([key])
		else:
			cache_values[key][0] += 1
			cache_values[key][1] = value
			#need to locate key in cache
			#then check if the key in cache needs to be moved to another level


def main():
	set(1, "1")			# [[1]]
	set(2, "1")			# [[1, 2]]
	set(2, "2")			# [[2], [1]]
	set(2, "3")			# [[2], [1]]
	set(3, "1")			# [[2], [1, 3]]
	set(3, "2")			# [[2], [3], [1]]
	set(3, "3")			# [[2, 3], [1]]
	set(3, "4")			# [[3], [2], [1]]
	set(3, "5")			# [[3], [2], [1]]

