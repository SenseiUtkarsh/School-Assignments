import pickle
def MENU():
    print("1. Add Student Record")
    print("2. Remove Student Record")
    print("3. Search Student in Record")
    print("4. Submit fees of Student")
    print("5. Add a new Teacher")
    print("6. Remove the Teacher From School!")
    print("7. Update Teachers Salary!")

def AddSt():
    fw = open("Student.dat" , 'wb')
    n=input("name: " ).capitalize()
    cl= input("Class : ")
    r= input("Roll no: ") 
    a=input("Address :")
    ph=input("Phone : ")
    data = [n , cl , r , a , ph ]
    pickle.dump(data , fw) 
    fw.close()
    print('Data updated!..') 
    print(data)
def RemoveSt():
    frm = open("student.dat" , "rb+")
    data = pickle.load(frm)
    frm.close()
    roll = input('Roll ')
    frm = open("student.dat" , "wb")
    # print(data)
    rmvst = []
    for i in data:
        if i[0] == roll :
            continue # leave the data which you want to delete!
        rmvst.append(i)
    pickle.dump(rmvst , frm)
    print(rmvst)
    print("Record deleted successfully..")
    frm.close
    
#------
def SearchStd():
    fr = open("student.dat" , 'rb')
    name = input("Enter name to be searched ").capitalize()
    data = pickle.load(fr)
    for names in data :
        if name in data:
            print(name , data)
            print('record found')
            break
    else:
        print("No Record!...")
    fr.close()
def SubmitFee():
    fs = open("student.dat" , 'ab')
    name = input("Student Name ").capitalize()
    month = input('Enter the month ')
    status ="Submited!"
    record = [name , month , status ]
    pickle.dump(record , fs)
    print(record)
    print('SUCCESSFUL!')


def AddTeacher():
    ft = open("Teacher.dat" , 'wb')
    Ecode = int(input("Teacher Code : "))
    nm = input("Teacher name : ")
    s = int(input("Salary: "))
    a = input("Address :")
    ph = input("Phone :")
    data= [ Ecode , nm , s , a , ph]
    pickle.dump(data , ft)
    print(data)
    print('Teacher Added Successfully')
    ft.close()

def RemoveTec():
    frmt = open("student.dat" , "rb+")
    data=pickle.load(frmt)
    frmt.close()
    code = input('Teachers code ')
    frmt = open("Teacher.dat" , "wb")
    # print(data)
    rmvt = []
    for i in data:
        if i[0] == code :
            continue # leave the data which you want to delete!
        rmvt.append(i)
    pickle.dump(rmvt , frmt)
    print("Record deleted successfully..")
    frmt.close


def UpdateSa():
    fwt = open("Teacher.dat" , 'wb')
    n=input("Teacher : ")
    tcode=int(input(" Tcode : "))
    salary=int(input(" Salary : "))
    data= [n , tcode]
    pickle.dump(data , fwt)
    print("Data updated!")
    fwt.close()


