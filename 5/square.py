class Square:
	def __init__(self,num):
			self.val=num
	def cal_square(self):
		return(self.val*self.val)
		
num=int(input("Enter A Number:"))
s=Square(num)
print("Square=",s.cal_square())
		