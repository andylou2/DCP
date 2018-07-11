def first_missing(input):
	#line up better with 0-indexed arrays
	for i in range(len(input)):
		input[i]-=1
	
	for i in range(len(input)):
		while input[i] >= 0 and input[i] < len(input) and\
			  input[i] != i and input[input[i]] != input[i]:
			swap(input, i, input[i])
	
	for i, val in enumerate(input):
		if i != val:
			return i+1
	return len(input)+1

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	
input0 = [0,5,3,2,4]

print(first_missing(input0))