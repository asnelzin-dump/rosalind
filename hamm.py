from sys import argv

dna1, dna2 = open(argv[1]).readlines()
distance = 0

for i in range(len(dna1)):
	if dna1[i] != dna2[i]:
		distance += 1

print(distance)