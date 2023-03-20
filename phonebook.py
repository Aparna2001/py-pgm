#without using function 

ph={}
c=1
while c==1:
    print("Options:")
    print("1.Create\n2.View\n3.Edit\n4.Delete\n5.Exit")
    o=int(input("Enter your choice "))
    if o==1:
        n=input("Enter name ")
        e=input("Enter emailid ")
        co=input("Are there 2 phone numbers ")
        if co=='yes':
            p1=int(input("Enter phone number1 "))
            p2=int(input("Enter phone number2 "))
            ph[n]={"name":n ,"phoneno":[p1,p2] ,"email":e }
        else:
            p=int(input("Enter phone number "))
            ph[n]={"name":n ,"phoneno":[p] ,"email":e }
        print(ph)
    elif o==2:
        a=input("Enter contact to be viewed ")
        print(ph[a])
    elif o==3:
        a=input("Enter contact to be edited ")
        x=input("Enter what is to be edited(phone no: or emailid or name) ")
        if x=='phoneno:':
            if len(ph[a]["phoneno"])==1:
                y=int(input("Enter new number "))
                ph[a]["phoneno"]=y
            else:
                q=int(input("Enter which number is to be edited(1 or 2) "))
                if q==2:
                    y=int(input("Enter new number "))
                    ph[a]["phoneno"][1]=y
                else:
                    y=int(input("Enter new number "))
                    ph[a]["phoneno"][0]=y 
            print("Edited contact is: ",end="  ")
            print(ph[a])
        elif x=='emailid' :
            e=input("Enter new emailid ")
            ph[a]["email"]=e
            print("Edited contact is: ",end="  ")
            print(ph[a])
        else:
            newname=input("Enter new name ")
            no=ph[a]["phoneno"]
            em=ph[a]["email"]
            ph[newname]={"name":newname ,"phoneno":no ,"email":em}
            ph.pop(a)
            print("Edited contact is: ",end="  ")
            print(ph[newname])
        
        
    elif o==4:
        a=input("Enter contact to be deleted ")
        ph.pop(a)
        print("Phonebook after deleting the said contact is :")
        print(ph)
    elif o==5:
        c=0
    else:
        print("Invalid choice")





# using function

def create():
    n=input("Enter name ")
    e=input("Enter emailid ")
    co=input("Are there 2 phone numbers ")
    if co=='yes':
        p1=int(input("Enter phone number1 "))
        p2=int(input("Enter phone number2 "))
        ph[n]={"name":n ,"phoneno":[p1,p2] ,"email":e }
    else:
        p=int(input("Enter phone number "))
        ph[n]={"name":n ,"phoneno":[p] ,"email":e }
    print(ph)

def view():
    a=input("Enter contact to be viewed ")
    print(ph[a])

def edit():
    a=input("Enter contact to be edited ")
    x=input("Enter what is to be edited(phone no: or emailid or name) ")
    if x=='phoneno:':
        if len(ph[a]["phoneno"])==1:
            y=int(input("Enter new number "))
            ph[a]["phoneno"]=y
        else:
            q=int(input("Enter which number is to be edited(1 or 2) "))
            if q==2:
                y=int(input("Enter new number "))
                ph[a]["phoneno"][1]=y
            else:
                y=int(input("Enter new number "))
                ph[a]["phoneno"][0]=y 
        print("Edited contact is: ",end="  ")
        print(ph[a])
    elif x=='emailid' :
        e=input("Enter new emailid ")
        ph[a]["email"]=e
        print("Edited contact is: ",end="  ")
        print(ph[a])
    else:
        newname=input("Enter new name ")
        no=ph[a]["phoneno"]
        em=ph[a]["email"]
        ph[newname]={"name":newname ,"phoneno":no ,"email":em}
        ph.pop(a)
        print("Edited contact is: ",end="  ")
        print(ph[newname])

def delete():
    a=input("Enter contact to be deleted ")
    ph.pop(a)
    print("Phonebook after deleting the said contact is :")
    print(ph)

ph={}
c=1
while c==1:
    print("Options:")
    print("1.Create\n2.View\n3.Edit\n4.Delete\n5.Exit")
    o=int(input("Enter your choice "))
    if o==1:
        create()
    elif o==2:
        view()
    elif o==3:
        edit()        
    elif o==4:
        delete()
    elif o==5:
        c=0
    else:
        print("Invalid choice")

#using class

dic={}
class Phonebook:
    def __init__(self):
        self.ph={}
    def create(self,n,ph,em):
        self.name=n
        self.phone=ph
        self.email=em
        self.ph={'name ':self.name, 'phoneno: ':self.phone, 'email ':self.email}
        dic[n]=self.ph
        print(dic)
    def view(self,vn):
        print(dic[vn])
    def edit(self):
        a=input("Enter contact to be edited ")
        x=input("Enter what is to be edited(phone no: or emailid or name) ")
        if x=='p':
            y=int(input("Enter new number "))
            dic[a]["phoneno: "]=y
            print("Edited contact is: ",end="  ")
            print(dic[a])
        elif x=='e':
            e=input("Enter new emailid ")
            dic[a]["email "]=e
            print("Edited contact is: ",end="  ")
            print(dic[a])
        else:
            nn=input("Enter new name: ")
            on=dic[a]["phoneno: "]
            oe=dic[a]["email "]
            dic.pop(a)
            dic[nn]={'name ':nn, 'phoneno: ':on, 'email ':oe}
            print("Edited contact is: ",end="  ")
            print(dic[nn])
    def delete(self):
        a=input("Enter contact to be deleted ")
        dic.pop(a)
        print("Phonebook after deleting the said contact is :")
        print(dic)
c=1
while c==1:
    print("Options:")
    print("1.Create\n2.View\n3.Edit\n4.Delete\n5.Exit")
    o=int(input("Enter your choice "))
    con=Phonebook()
    if o==1:
        n=input("Enter name: ")
        ph=int(input("Enter phone number: "))
        em=input("Enter email: ")
        con.create(n,ph,em)
    elif o==2:
        a=input("Enter contact to be viewed: ")
        con.view(a)
    elif o==3:
        con.edit()        
    elif o==4:
        con.delete()
    elif o==5:
        c=0
    else:
        print("Invalid choice")