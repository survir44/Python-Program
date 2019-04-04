def arithmetic(ch):
	if(ch==1 or ch==2 or ch==3 or ch==4):
		a=int(input("\nEnter First Number:"))
		b=int(input("Enter Second Number:"))
		if(ch==1):
			print(a+b)
		elif(ch==2):
			print(a-b)
		elif(ch==3):
			print(a*b)
		else:
			if(b==0):
				print("Can't Divide By Zero")
			else:
				print(a/b)
	else:
		print("\nWrong Choice Entered")
			
print("Arithmetic Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("Enter Your Choice:"))
arithmetic(ch)
opt=int(input("Press 1 For Continue Otherwise 0:"))

while(opt==1):
	print("\nArithmetic Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
	ch=int(input("Enter Your Choice:"))
	arithmetic(ch)
	opt=int(input("Press 1 For Continue Otherwise 0:"))

	
	
