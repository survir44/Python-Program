l=[]
def insert():
	index=int(input("\nEnter The Index:"))
	val=int(input("Enter Value:"))
	l.insert(index,val)
	print("\n",l)

def append():
	val=int(input("Enter Value:"))
	l.append(val)
	print("\n",l)

def copy():
	l1=[]
	l1=l.copy()
	print("\nMain List",l)
	print("Copied List",l1)

def count():
	val=int(input("Enter Value:"))
	print("\nCount=",l.count(val))

def index():
	val=int(input("Enter Value:"))
	print("\nPosition=",l.index(val))

while(True):
	ch=int(input("\n******MENU*******\n1.Insert\n2.Append\n3.Pop\n4.Copy\n5.Count\n6.Reverse\n7.Sort\n8.Index\n9.Clear\n10.Exit\nEnter Your Choice:"))
	if(ch==1 or ch==2 or ch==3 or ch==4 or ch==5 or ch==6 or ch==7 or ch==8 or ch==9 or ch==10):
		if(ch==1):
			insert()
		elif(ch==2):
			append()
		elif(ch==3):
			l.pop()
			print("\n",l)
		elif(ch==4):
			copy()
		elif(ch==5):
			count()
		elif(ch==6):
			l.reverse()
			print("\n",l)
		elif(ch==7):
			l.sort()
			print("\n",l)
		elif(ch==8):
			index()
		elif(ch==9):
			l.clear()
			print("\n",l)
		elif(ch==10):
			exit()
	else:
		print("\nWrong Choice Entered")