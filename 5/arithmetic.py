class Arithmetic:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def addition(self):
		return(self.a+self.b)
	def subtraction(self):
		return(self.a-self.b)
	def multiplication(self):
		return(self.a*self.b)
	def division(self):
		if(self.b==0):
			return("\nCan not Divide By Zero")
		else:
			return(self.a/self.b)

while(True):
	ch=int(input("MENU\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter Your Choice:"))
	if(ch==1 or ch==2 or ch==3 or ch==4):
		a=int(input("\nEnter First Number:"))
		b=int(input("Enter Second Number:"))
		a=Arithmetic(a,b)
		if(ch==1):
			print(a.addition())
		elif(ch==2):
			print(a.subtraction())
		elif(ch==3):
			print(a.multiplication())
		else:
			print(a.division())
	else:
		print("\nWrong Choice Entered")
	opt=int(input("\nPress 1 For Continue Otheriwise 0:"))
	if(opt==0):
		break
		
			
