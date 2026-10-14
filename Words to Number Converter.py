P=['Hundered', 'Thousand',' ', 'Lakh',' ', 'Crore']
Str = input('Enter Number in Words(Max Limit 99,99,99,999):\n') 
N= [0,1,2,3,4,5,6,7,8,9]
LN = ['Zero', 'One', "Two", "Three", "Four", 'Five', 'Six', "Seven", "Eight", "Nine"]
T1=[' ',' ', "Tw", "Th", 'Fo', 'Fi', 'Si', "Se", "Ei", "Ni"]
T2= ["et", "ty"]
Number = 0
S=Str.split(' ')
for i in S:
	if i in LN:
		n=N[LN.index(i)] 
		if len(S)-1 != S.index(i) and S[S.index(i)+1] in P:
			n = n*(10**(P.index(S[S.index(i)+1])+2)) 
		Number += n
	elif i[:2] in T1 and i[-2:] != 'nd': 
		n= N[T1.index(i[:2])] 
		if T2.index(i[-2:])==0:
			n=n+10
		elif T2.index(i[-2:])==1: 
			n=n*10
		else: 
			n=n+10
		
		if (S.index(i) != len(S)-1 and S. index(i) != len(S)-2) and ((S[S.index(i)+1] in LN and S[S.index(i)+2] in P) or S[S.index(i)+1] in P):
			if S[S.index(i)+1] in P:
				n *= 10**(P.index(S[S.index(i)+1])+2) 
			else:
				n += N[LN.index(S[S.index(i)+1])]
				n *= 10**(P.index(S[S.index(i)+2])+2)
				S[S.index(i)+1] = ''
				S[S.index(i)+2] = ''
		Number += n
	else:
		if i == 'Eleven':
			n=11
			if len(S)-1 != S.index(i) and S[S.index(i)+1] in P:
				n = n*(10**(P.index(S[S.index(i)+1])+2))
			Number += n
		elif i== 'Ten':
			n= 10
			if len(S)-1 != S.index(i) and S[S.index(i)+1] in P:
				n = n*(10**(P.index(S[S.index(i)+1])+2))
			Number += n
	S[S.index(i)] = ''
print('Conversion in Number:',Number)