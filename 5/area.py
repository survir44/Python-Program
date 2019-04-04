class Circle:
	def __init__(self,r):
		self.r=r
	def area(self):
		print("Area=",3.14*self.r*self.r)
	def perimeter(self):
		print("Perimeter=",6.28*self.r)

r=int(input("Enter Radius Of A Circle:"))
c=Circle(r)
c.area()
c.perimeter()
