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

def in_new_alphabet(s, alphabet):
	new_s = ""
	for c in s:
		new_s += alphabet[c]
	return new_s

def main():
	try:
		in_file = open(argv[1], 'r')
		try:
			data = [s.replace('\n', '') for s in in_file.readlines()]
		finally:
			in_file.close()
	except IOError:
		print("Cant open file or read data")
		data = [s.replace('\n', '') for s in stdin.readlines()]

	alphabet = data[0].split()
	k = len(alphabet)
	max_n = int(data[1])

	result_strings = []

	for n in range(1, max_n + 1):
		result_strings += get_all_numbers(alphabet, k, n)

	new_alphabet = dict(zip( alphabet, map(chr, range(65, 91)) ))

	result_strings = [(s, in_new_alphabet(s, new_alphabet)) for s in result_strings]

	result_strings.sort(key = lambda x: x[1])

	try:
		out_file = open("lexv_out.txt", 'w')
		try:
			for s in result_strings:
				print(s[0], file = out_file)
		finally:
			out_file.close()
	except IOError:
		print("Cant write data")


if __name__ == "__main__":
	main()