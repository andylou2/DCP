def justify(input, k):
	
	words = input.split(" ")
	lines = [[]]
	line_len = -1;
	for word in words:
		if line_len+len(word)+1 >=k:
			lines.append([])
			line_len = -1
		lines[-1].append(word)
		line_len+=len(word)+1
	return [justify_line(line,k) for line in lines]
		
		
	

def justify_line(line, k):
	num_words = len(line)
	if num_words == 1:
		return line
	num_chars = sum([len(word) for word in line])
	num_spaces = k - num_chars
	for i in range(num_spaces%(num_words-1)):
		line[i]+=" "
	return (" "*(num_spaces/(num_words-1))).join(line)
	
# print(justify_line(["the","quick","brown"],20))
for line in justify("the quick brown fox jumps over the lazy dog",16):
	print(line)