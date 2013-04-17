from operator import itemgetter

def count_of_symbol(c, str):
	counter = 0
	for i in str:
		if i == c:
			counter += 1
	return counter

def gc(dna):
	return ((count_of_symbol("G", dna) + count_of_symbol("C", dna)) * 100) / len(dna)

def get_max_gc(data):
	for i, dna in enumerate(data):
		data[i] = (dna[0], dna[1], gc(dna[1]))

	return sorted(data, key = itemgetter(2), reverse = True)[0]

def main():
	try:
		f = open("/home/asnelzin/Загрузки/rosalind_gc (1).txt", "r")
		try:
			raw_data = f.readlines()
			raw_data = [s.replace('\n', '') for s in raw_data]
			data = []
			dna = ""
			num = raw_data[0][-4:]
			for line in raw_data[1:]:
				if '>' in line:
						data.append( (num, dna) )
						dna = ""
						num = line[-4:]
				else:
					dna += line
			data.append( (num, dna) )
			
		finally:
			f.close()
	except IOError:
		print("Error: Can't find file or read data")
	
	num, dna, gc = get_max_gc(data)
	print("Rosalind_{0}\n{1}".format(num, gc))

if __name__ == "__main__":
	main()