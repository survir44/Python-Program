import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="oracle",database="employee")
mycur=mycon.cursor()

def display():
	mycur.execute("SELECT * FROM employee_info")
	record=mycur.fetchall()
	print("")
	print(record)

def insert():
	val=[]
	val.append(input("\nEnter Employee ID:"))
	val.append(input("Enter Employee Name:"))
	val.append(input("Enter Deptartment:"))
	val.append(input("Enter Gender:"))
	val.append(input("Enter Phone:"))
	sql="INSERT INTO employee_info VALUES(%s,%s,%s,%s,%s)"
	mycur.execute(sql,val)
	mycon.commit()
	display()

def delete():
	val=[]
	val.append(input("Enter Employee ID:"))
	sql="DELETE FROM employee_info WHERE eid=%s"
	mycur.execute(sql,val)
	mycon.commit()
	display()

def update():
	val=[]
	val.append(input("\nEnter Employee Name:"))
	val.append(input("Enter Deptartment:"))
	val.append(input("Enter Gender:"))
	val.append(input("Enter Employee ID:"))
	sql="UPDATE employee_info SET ename=%s,dept=%s,gender=%s WHERE eid=%s"
	mycur.execute(sql,val)
	mycon.commit()
	display()

while(True):
	print("\nMENU\n1.INSERT\n2.DELETE\n3.UPDATE\n4.DISPLAY\n5.EXIT")
	ch=int(input("Enter Your Choice:"))
	if(ch==1):
		insert()
	elif(ch==2):
		delete()
	elif(ch==3):
		update()
	elif(ch==4):
		display()
	elif(ch==5):
		exit()
	else:
		print("Wrong Choice Entered")
	
	

