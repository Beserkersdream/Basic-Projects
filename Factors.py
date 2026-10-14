n = int(input("Enter a no. to know it's factors: "))
print("Factors of",n,'are-: ',end='')
for i in range(2,n//2+1):
	if n%i == 0:
		print(i,end=' ')
print(n)