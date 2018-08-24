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
	for i, x in enumerate(message):
		
		#make sure to not break up a 10 or 20
		if (i<2 or message[i-2]!='0') and message[i:i+2][::-1] in valid_pairs:
			temp = curr+prev
			prev = curr
			curr = temp
		else:
			prev = curr
	return curr
	
print(decode('1119911'))
			
		
			