def fibonacci(t,f,s,th):
	if(t>2):
		th=f+s
		print(th,"",end='')
		f=s
		s=th
		t=t-1
		fibonacci(t,f,s,th)

term=int(input("Enter Number Of Terms:"))
if(term==1):
	print("0",end='')
elif(term>0):
	print("0 1 ",end='')
	fibonacci(term,0,1,1)
else:
	print("Wrong Term Entered")