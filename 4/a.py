string=input("Enter A String:")
count=0
l=len(string)
string=string.lower()
for i in range(0,l):
	if(string[i]=='a'):
		count=count+1
print("Number Of A's=",count)