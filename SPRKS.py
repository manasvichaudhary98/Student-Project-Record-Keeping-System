import pymysql as m1
import sys

con=m1.connect(host="localhost", user="root", password="school", database="student_record_system")

if con.open:
    print("Connected Successfully")
else:
    print("Connection Failed")

uname=input("Enter your username: ")
pwd=input("Enter your password: ")

if uname=="admin" and pwd=="school":
    print("Login Successful")
    print("Welcomeee")
else:
    print("Invalid Username or Password")
    sys.exit(0)
     
print(" ♡ STUDENT RECORD KEEPING SYSTEM ☆")

def StudentModule():
    while True:
        print("Student Details Module")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display Students")
        print("6. Back")
        choice=int(input("Enter your choice: "))
        if choice==1:
            sid=int(input("Enter Student ID: "))
            bid=int(input("Enter Batch ID: "))
            sname=input("Enter Student Name: ")
            fname=input("Enter  father's name: ")
            gender=input("Enter Gender(F/M): ")
            dob=input("Enter Date of Birth (DD/MM/YYYY): ")
            mobno=int(input("Enter Mobile Number: "))
            email=input("Enter your email id: ")
            add=input("Enter your house address: ")
            course=input("Enter Course: ")
            addate=input("Enter admission date: ")
            qry="insert into student values({}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(sid,bid,sname,
            fname,gender,dob,mobno,email,add,course,addate)
            cursor=con.cursor()
            cursor.execute(qry)
            con.commit()
            print("Student Record Added Successfully")

        elif choice==2:
            sid=int(input("Enter Student ID to Search: "))
            qry="select * from student where Student_ID={}".format(sid)
            cursor=con.cursor()
            cursor.execute(qry)
            data=cursor.fetchall()
            if len(data)==0:
                print("Student ID does not exist")
            else:
                for row in data:
                    print(row)
                
        elif choice==3:
            while True:
                print('What do you want to update?')
                print("1. Update Name")
                print("2. Update Course")
                print("3. Update Mobile Number")
                print("4. Back")
                uch=int(input("Enter choice: "))
                if choice==1:
                    sid=int(input("Enter Student ID: "))
                    newname=input("Enter New Name: ")
                    qry="update student set Name='{}' where Student_ID={}".format(newname,sid)
                    rows=cursor.execute(qry)
                    con.commit()
                    if rows==0:
                        print("Student ID does not exist")
                    else:
                        print("Name Updated")
                elif choice==2:
                    sid=int(input("Enter Student ID: "))
                    newcourse=input("Enter New Course: ")
                    qry="update student set Course='{}' where Student_ID={}".format(newcourse,sid)
                    rows=cursor.execute(qry)
                    con.commit()
                    if rows==0:
                        print("Student ID does not exist")
                    else:
                        print("Course Updated")
                elif choice==3:
                    sid=int(input("Enter Student ID: "))
                    newmob=input("Enter New Mobile Number: ")
                    qry="update student set Mobile_No='{}' where Student_ID={}".format(newmob,sid)
                    rows=cursor.execute(qry)
                    con.commit()
                    if rows==0:
                        print("Student ID does not exist")
                    else:
                        print("Mobile No. Updated")
                elif choice==4:
                     break
                else:
                    print("invalid choice")
        
        elif choice==4:
            sid=int(input("Enter Student ID to Delete: "))
            qry="delete from student where Student_ID={}".format(sid)
            cursor=con.cursor()
            cursor.execute(qry)
            con.commit()
            if rows==0:
                print("Student ID does not exist")
            else:
                print("Student Record Deleted Successfully")
            
        elif choice==5:
            qry="select * from student"
            cursor=con.cursor()
            cursor.execute(qry)
            data=cursor.fetchall()
            for row in data:
                print(row)

        elif choice==6:
            break
                
        else:
            print("invalid choice!")
            
def BatchModule():
    while True:
        print("Batch Details Module")
        print("1. Create Batch")
        print("2. Search Batch")
        print("3. Update Batch")
        print("4. Delete Batch")
        print("5. Display Batches")
        print("6. Back")
        choice=int(input("Enter your choice: "))
        if choice==1:
            bid=int(input("Enter Batch ID: "))
            bname=input("Enter Batch Name: ")
            cname=input("Enter Course Name: ")
            sdate=input("Enter Start Date: ")
            edate=input("Enter End Date: ")
            timing=input("Enter Timing: ")
            faculty=input("Enter Faculty Name: ")
            nostd=int(input("Enter Number of Students: "))
            qry="""insert into batch
            values({},'{}','{}','{}','{}','{}','{}',{})""".format(
            bid,bname,cname,sdate,edate,timing,faculty,nostd)
            cursor=con.cursor()
            cursor.execute(qry)
            con.commit()
            print("Batch Added Successfully")

        elif choice==2:
            bid=int(input("Enter Batch ID to Search: "))
            qry="select * from batch where Batch_ID={}".format(bid)
            cursor=con.cursor()
            cursor.execute(qry)
            data=cursor.fetchall()
            for row in data:
                print(row)

        elif choice==3:
            bid=int(input("Enter Batch ID: "))
            newtiming=input("Enter New Timing: ")
            qry="update batch set Timing='{}' where Batch_ID={}".format(newtiming,bid)
            cursor=con.cursor()
            cursor.execute(qry)
            con.commit()
            print("Batch Updated")

        elif choice==4:
            bid=int(input("Enter Batch ID to Delete: "))
            qry="delete from batch where Batch_ID={}".format(bid)
            cursor=con.cursor()
            cursor.execute(qry)
            con.commit()
            print("Batch Deleted")

        elif choice==5:
            qry="select * from batch"
            cursor=con.cursor()
            cursor.execute(qry)
            data=cursor.fetchall()
            for row in data:
                print(row)

        elif choice==6:
            break

        else:
            print("invalid choice")

        
def FeeModule():
    print("Fee Details Module")
    print("1. Record Fee Payment")
    print("2. View Fee Details")
    print("3. Search Fee Record")
    print("4. Update Fee Record")
    print("5. Generate Fee Due List")
    print("6. Generate Fee Receipt")
    choice=int(input("Enter your choice: "))
    if choice==1:
        rno=int(input("Enter Receipt Number: "))
        sid=int(input("Enter Student ID: "))
        total=float(input("Enter Total Fee: "))
        paid=float(input("Enter Amount Paid: "))
        balance=total-paid
        pdate=input("Enter Payment Date: ")
        pmode=input("Enter Payment Mode: ")
        inst=int(input("Enter Installment Number: "))
        remarks=input("Enter Remarks: ")
        qry="insert into fee values({}, {}, {}, {}, {}, '{}', '{}', {}, '{}')".format(rno,sid,total,paid
        ,balance,pdate,pmode,inst,remarks)
        cursor=con.cursor()
        cursor.execute(qry)
        con.commit()
        print("Fee Record Added Successfully")

    elif choice==2:
         qry="select * from fee"
         cursor=con.cursor()
         cursor.execute(qry)
         data=cursor.fetchall()
         for row in data:
             print(row)

    elif choice==3:
        sid=int(input("Enter Student ID: "))
        qry="select * from fee where Student_ID={}".format(sid)
        cursor=con.cursor()
        cursor.execute(qry)
        data=cursor.fetchall()
        for row in data:
            print(row)

    elif choice==4:
        rno=int(input("Enter Receipt Number: "))
        paid=float(input("Enter New Amount Paid: "))
        qry="update fee set Amount_Paid={} where Receipt_No={}".format(paid,rno)
        cursor=con.cursor()
        cursor.execute(qry)
        con.commit()
        print("Fee Record Updated")

    elif choice==5:
        qry="select * from fee where Balance_Fee>0"
        cursor=con.cursor()
        cursor.execute(qry)
        data=cursor.fetchall()
        print("Students Having Fee Due:")
        for row in data:
            print(row)

    elif choice==6:
         rno=int(input("Enter Receipt Number: "))
         qry="select * from fee where Receipt_No={}".format(rno)
         cursor=con.cursor()
         cursor.execute(qry)
         data=cursor.fetchall()
         for row in data:
             print("="*40)
             print("FEE RECEIPT")
             print("="*40)
             print("Receipt No :",row[0])
             print("Student ID :",row[1])
             print("Total Fee  :",row[2])
             print("Paid Amount:",row[3])
             print("Balance Fee:",row[4])
             print("Payment Date:",row[5])
             print("Payment Mode:",row[6])
             print("Installment :",row[7])
             print("Remarks :",row[8])
             print("="*40)

def ReportModule():
    print("Report Details Module")
    print("1. Student Report")
    print("2. Batch Report")
    print("3. Fee Report")
    choice=int(input("Enter your choice: "))
    cursor=con.cursor()
    if choice==1:
        cursor.execute("select * from student")
        for row in cursor.fetchall():
            print(row)

    elif choice==2:
        cursor.execute("select * from batch")
        for row in cursor.fetchall():
            print(row)

    elif choice==3:
        cursor.execute("select * from fee")
        for row in cursor.fetchall():
            print(row)

    else:
        print("Invalid Choice")

while True:
    print("Main Menu")
    print("1. Student Details Module")
    print("2. Batch Details Module")
    print("3. Fee Details Module")
    print("4. Reports")
    print("5. Exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        StudentModule()

    elif choice==2:
        BatchModule()

    elif choice==3:
        FeeModule()

    elif choice==4:
        ReportModule()

    elif choice==5:
        sys.exit(0)

    else:
        print("invalid choice!")
