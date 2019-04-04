size=int(input("Enter Size Of List:"))
l=[]
for i in range(0,size):
	l.append(int(input("Enter A Element:")))
min=l[0]
max=l[0]
for i in range(0,size):
	if(min>l[i]):
		min=l[i]
	elif(max<l[i]):
		max=l[i]
print("Minimum=",min,"\nMaximum=",max)
