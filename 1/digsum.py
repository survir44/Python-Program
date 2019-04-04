num=int(input("Enter A Number:"))
sum=0
while(num!=0):
	dig=num%10
	sum+=dig
	num=num//10
print("Sum=",sum)