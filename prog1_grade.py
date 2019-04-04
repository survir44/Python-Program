sub1 = input("Enter marks of subject1: ")
sub2 = input("Enter marks of subject2:")
sub3 = input("Enter marks of subject3:")
tot = sub1+sub2+sub3
print "Total marks = " , tot

if tot/3>80:
	print "Grade = A"
elif tot/3>60:
	print "Grade = B"
elif tot/3>35:
	print "Grade = c"
else:
	print "Grade = F"
