string1=input("Enter A String:")
l=len(string1)
print()
for i in range(0,l):
	if(string1[i].isalpha() or string1[i]==' '):
		print(string1[i],end='')