n1 = input("Enter the First no.: ")
n2 = input("Enter the Second no.: \n")
while 1:
#print "Enter your choice"
	print "Addition - 1"
	print "Subtraction - 2"
	print "Multiplication - 3"
	print "Division - 4"
	print "Mod - 5"
	print "Exit - 0"
	n = input("Enter your choice: ")
	if n == 1:
		print "Sum = ",n1+n2,"\n"
	elif n==2:
		print "difference = ",n1-n2,"\n"
	elif n==3:
		print "product = ",n1*n2,"\n"
	elif n==4:
		if n2!=0:
			print "quotient = ",n1/n2,"\n"
		else:
			print "Cannot Divide!!\n"
	elif n==5:
		if n2!=0:
			print "Remainder = ",n1%n2,"\n"
		else:
			print "Cannot Divide!!\n"
	elif n==0:
		print "Exit\n"
		break;
	else:
		print "Invalid Choice!\n"
