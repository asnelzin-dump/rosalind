from sys import stdin, argv

def number_to_string(num, alphabet):
	s = map(lambda x : alphabet[x] , num)
	return ''.join(s)

def next_number(num, k):
	if num[-1] == k-1:
		for i, el in enumerate(reversed(num)):
			if el == k-1:
				num[-i-1] = 0
			else:
				num[-i-1] += 1
				break
	else:
		num[-1] += 1
	return num

def get_all_numbers(alphabet, k, n):
	num = [0 for i in range(n)]
	numbers = [number_to_string(num, alphabet)]
	for i in range(1, k**n):
		num = next_number(num, k)
		numbers.append( number_to_string(num, alphabet) )
	return numbers

def main():
	data = None
	try:
		in_f = open(argv[1], 'r')
		#f = stdin
		try:
			data = [i.replace('\n', '') for i in in_f.readlines()]
		finally:
			in_f.close()
	except IOError:
		print("Cant open file or read data!")

	if data != None:
		alphabet = data[0].split()
		k = len(alphabet)
		n = int(data[1])

		data_to_write = get_all_numbers(alphabet, k, n)

		try:
			out_f = open("lexf.out", 'w')
			try:
				for s in data_to_write:
					print(s, file = out_f)
			finally:
				out_f.close()
		except IOError:
			print("Cant write data!")

if __name__ == "__main__":
	main()