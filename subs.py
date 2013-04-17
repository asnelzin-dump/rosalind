from sys import stdin, argv

def subs(str, substr):
	substr_len = len(substr)
	str_len = len(str)
	result = []
	for left in range(str_len):
		for right in range(substr_len, str_len):
			if str[left:right] == substr:
				result.append(left + 1)
	return result

def main():
	data = None
	try:
		f = open(argv[1], 'r')
		#f = stdin
		try:
			data = [s.replace('\n', '') for s in f.readlines()]
		finally:
			f.close()
	except IOError:
		print('Can\'t open file or read data')

	if data != None:
		print(*subs(data[0], data[1]), sep = ' ') 

if __name__ == '__main__':
	main()