from collections import Counter
from sys import argv

def mrna(prot, table):
	number_rnas = 1
	for aa in prot:
		number_rnas *= table[aa]
	number_rnas *= table["Stop"]
	return number_rnas

def main():

	table = {"UUU":"F",   "CUU":"L",      "AUU":"I",      "GUU":"V",
         	 "UUC":"F",   "CUC":"L",      "AUC":"I",      "GUC":"V",
             "UUA":"L",   "CUA":"L",      "AUA":"I",      "GUA":"V",
             "UUG":"L",   "CUG":"L",      "AUG":"M",      "GUG":"V",
             "UCU":"S",   "CCU":"P",      "ACU":"T",      "GCU":"A",
             "UCC":"S",   "CCC":"P",      "ACC":"T",      "GCC":"A",
             "UCA":"S",   "CCA":"P",      "ACA":"T",      "GCA":"A",
             "UCG":"S",   "CCG":"P",      "ACG":"T",      "GCG":"A",
             "UAU":"Y",   "CAU":"H",      "AAU":"N",      "GAU":"D",
             "UAC":"Y",   "CAC":"H",      "AAC":"N",      "GAC":"D",
             "UAA":"Stop","CAA":"Q",      "AAA":"K",      "GAA":"E",
             "UAG":"Stop","CAG":"Q",      "AAG":"K",      "GAG":"E",
             "UGU":"C",   "CGU":"R",      "AGU":"S",      "GGU":"G",
             "UGC":"C",   "CGC":"R",      "AGC":"S",      "GGC":"G",
             "UGA":"Stop","CGA":"R",      "AGA":"R",      "GGA":"G",
             "UGG":"W",   "CGG":"R",      "AGG":"R",      "GGG":"G" }

    #input from file
	table_counter = Counter(table.values())
	prot = None
	try:
		f = open(argv[1], 'r')
		try:
			prot = f.readline()[:-1]
		finally:
			f.close()
	except IOError:
		print("Can't open file or read data")
	#prot = input()

	if prot != None:
		print(str(mrna(prot, table_counter))[-6:])


if __name__ == "__main__":
	main()