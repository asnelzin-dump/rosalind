#!/usr/bin/python3

input_string = open("/home/asnelzin/Загрузки/rosalind_revc.txt").readline()
out_string = ""

for c in input_string:
	if c == "A":
		out_string += "T"
	elif c == "T":
		out_string += "A"
	elif c == "C":
		out_string += "G"
	elif c == "G":
		out_string += "C"

print(out_string[::-1])