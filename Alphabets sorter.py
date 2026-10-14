print('This program is for arranging Alphabets...')
n = int(input('Enter no.of letters you want to arrange: '))
L = []
for i in range(n):
	a = input('Enter '+str(i+1)+'th letter: ')
	if len(a) == 1:
		if i == 0:
			L.append(a)
			continue
		else:
			for j in range(len(L)):
				if ord(a) < ord(L[j]):
					L.insert(j,a)
					break
				elif ord(a) > ord(L[len(L)-1- j]):
					if j+1 != len(L):
						L.insert(len(L)-j,a)
						break
					else:
						L.append(a)
						break
print((str(L).replace('[','')).replace(']',''))