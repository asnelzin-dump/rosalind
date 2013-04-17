dna1, dna2 = open("/home/asnelzin/Загрузки/rosalind_hamm (1).txt").readlines()
distance = 0

for i in range(len(dna1)):
	if dna1[i] != dna2[i]:
		distance += 1

print(distance)