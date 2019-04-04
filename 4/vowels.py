string=input("Enter A String:")
count=0
l=len(string)
string=string.lower()
for i in range(0,l):
	if(string[i]=='a'or string[i]=='e'or string[i]=='i'or string[i]=='o'or string[i]=='u'):
		count=count+1
print("Number Of Vowels=",count)