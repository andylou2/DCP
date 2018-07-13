valid_pairs = {str(i) for i in range(11,27) if i != 20}
print(valid_pairs)


"""
9 1 1
9 11
If you have 9911, there are two ways you can process this
19911: 	1 9911 four ways 
		19 911
	
"""
def decode(message):
	prev = 1
	curr = 1
	
	#Due to how 0 must be handled, slightly easier to go from right to left
	message = ''.join(reversed(message))
	print(message[0:2])
	for i, x in enumerate(message):
		#impossible to take 0 as standalone 
		if x == '0':
			prev = curr
		#must be parsed as 10 or 20
		elif (i!= 0 and message[i-1] == '0') or (i>1 and message[i-2]=='0'):
			prev = curr
		#11-19, 21-26 with no trailing zero
		elif message[i:i+2][::-1] in valid_pairs:
			temp = curr+prev
			prev = curr
			curr = temp
		else:
			prev = curr
	return curr
	
print(decode('1109911'))
			
		
			