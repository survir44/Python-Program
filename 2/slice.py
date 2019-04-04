l=[]
for i in range(0,5):
	l.append(input("Enter A Element:"))
print("Different Slice Operation")
print("[0:5:]=",l[0:5:])
print("[::]=",l[::])
print("[2:4:1]=",l[2:4:1])
print("[0:5:2]=",l[0:5:2])
print("[-1:-4:-2]=",l[-1:-4:-2])