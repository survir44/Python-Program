class Feet:
	def __init__(self,feet,inch):
		self.feet=feet
		self.inch=inch
	def add(self,f1,f2,f3):
		f3.feet=f1.feet+f2.feet
		f3.inch=f1.inch+f2.inch
		if(f3.inch>12):
			f3.feet=f3.feet+(f3.inch//12)
			f3.inch=f3.inch%12	
		
print("Enter Mesauremnt 1 ")
feet1=int(input("Enter Feet="))
inch1=int(input("Enter Inches="))
print("\nEnter Mesauremnt 2 ")
feet2=int(input("Enter Feet="))
inch2=int(input("Enter Inches="))
f1=Feet(feet1,inch1)
f2=Feet(feet2,inch2)
f3=Feet(0,0)
f1.add(f1,f2,f3)
print("\nMeasurement 1 + Measurement 2")
print("Feet=",f3.feet,"\tInches=",f3.inch)
