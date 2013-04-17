from math import factorial

def next_permutation(p):
	k = None
	for i in range(len(p)-1, 0, -1):
		if p[i] > p[i-1]:
			k = i - 1
			break
	if k == None:
		return None
	else:
		l = None
		for j in range(k+1, len(p)):
			if p[j] > p[k]:
				l = j

		p[k], p[l] = p[l], p[k]
		
		temp_list = p[k+1:]
		temp_list.reverse()
		p = p[:k+1] + temp_list
		
		return p

def print_perm(f, p):
	f.write( ' '.join( [str(i) for i in p] ) + '\n' )

def main():
	f = open("out_perm.txt", 'w')
	n = int(input())
	p = list(range(1, n+1))
	f.write(str(factorial(n)) + '\n')
	while p != None:
		print_perm(f, p)
		p = next_permutation(p)
	f.close()
if __name__ == "__main__":
	main()