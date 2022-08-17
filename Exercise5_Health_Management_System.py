# Exercise 5 Health Management System
def ffile(fh):
    with open(file1,'w') as f:
        food=input("Type Here: ")
        f.write(str([str(getdate())])+':'+food+"\n")
        return ffile
def fexercise(fe):
    with open(file2,'a') as g:
        exer=input("Type Here: ")
        g.write(str([str(getdate())])+' : '+exer+"\n")
        return fexercise
def ffiler(ffr):
    with open(rffile,'r') as h:
        ff=h.read()
        print(ff)
def efiler(efr):
    with open(refile,'r') as i:
        ef=i.read()
        print(ef)

def getdate():
    import datetime
    return datetime.datetime.now()

name=['harry','anshul','manish']
print("\t\t Welcome To\n\t  Health Management System\n")
user=int(input("1.Enter Data\n2.Show Data\nEnter Option: "))
if user==1:
    usr=str(input("Enter Your Name: "))
    if name.count(usr)>0:   #check whether input name is present in list or not
        option=int(input("\n1.Food\n2.Exercise\nEnter Option: "))
        if option==1: 
            file1='f'+usr+'.txt'
            ffile(usr)
        elif option==2:
            file2='e'+usr+'.txt'
            fexercise(usr)
    else:
        print('your Data not found')
elif user==2:
    option1=int(input("\n1.Food\n2.Exercise\nEnter Option: "))
    usr1=str(input("Enter Your Name: "))
    if option1==1:
        rffile='f'+usr1+'.txt'
        ffiler(usr1)
    elif option1==2:
        refile='f'+usr1+'.txt'
        efiler(usr1)
    else:
        print("Choose Correct Options")
else:
    print("Choose Correct Options")
