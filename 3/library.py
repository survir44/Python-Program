def cal_fine(days):
	if(days<15):
		print("No fine")
	else:
		fine=(days-15)*5
		return(fine)
		
cat=int(input("Enter Book Category:"))
days=int(input("Enter Number Of Days Book Issued:"))
lost=input("Book Lost(Y/N):")
lost=lost.upper()
if(lost=='Y'):
	print("Fine=500")
else:
	print("Fine=",cal_fine(days))

