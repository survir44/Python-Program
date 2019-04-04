size=int(input("Enter Size Of List:"))
l=[]
flag=0
for i in range(0,size):
	l.append(int(input("Enter A Element:")))
num=int(input("Enter Element To Be Found:"))
for i in range(0,size):
	if(l[i]==num):
		flag=1
		break
if(flag==1):
	print("Element Found At Position:",i+1)
else:
	print("Element Not Found")	
