def add(feet1,inch1,feet2,inch2):
	feet3=feet1+feet2
	inch3=inch1+inch2
	if(inch3>12):
		feet3=feet3+(inch3//12)
		inch3=inch3%12	
	print("\nMeasurement 1 + Measurement 2")
	print("Feet=",feet3,"\tInches=",inch3)

print("Enter Mesauremnt 1 ")
feet1=int(input("Enter Feet="))
inch1=int(input("Enter Inches="))
print("\nEnter Mesauremnt 2 ")
feet2=int(input("Enter Feet="))
inch2=int(input("Enter Inches="))
add(feet1,inch1,feet2,inch2)
