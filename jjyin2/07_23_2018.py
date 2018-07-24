import re

input = 'dir\n\tsubdir\n\tsubdir2\n\t\tfile.ext'
input2 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
TAB_REGEX = re.compile(r"[\t]+")

def wrapper(input):
	files = input.split('\n')
	return longest_path(files)[1]
def longest_path(input):
	if not input:
		return [],0
	
	root, *input = input
	root_depth, root = parse_tabs(root)
	max_path = ""
	
	while input:
		curr_depth, _ = parse_tabs(input[0])
		if curr_depth <= root_depth: 
			break
		input, path = longest_path(input)
		max_path = max(max_path,path, key=lambda x: len(x))
	return input, root+'/'+max_path if max_path else root

def parse_tabs(path):
	tabs = TAB_REGEX.findall(path)
	tabs = tabs[0] if tabs else []
	return len(tabs), path[len(tabs):]
#wrapper(input)

print(input2)
max_path=wrapper(input2)
print("{0}, len={1}".format(max_path, len(max_path)))