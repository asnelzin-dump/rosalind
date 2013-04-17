from sys import stdin

def pper(n, k):
	result = 1
	for i in range(n - k + 1, n + 1):
		result *= i
	return result

def main():
	input_data = None
	try:
		f = open("/home/asnelzin/Загрузки/rosalind_pper.txt", 'r')
		try:
			input_data = f.readline()
		finally:
			f.close()
	except IOError:
		print("Can't open file or read data")

	if input_data != None:
		n, k = input_data.split()
		n, k = int(n), int(k)
		print(pper(n, k) % 1000000)


if __name__ == "__main__":
	main()