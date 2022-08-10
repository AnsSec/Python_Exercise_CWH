'''Design a calculator which will correctly solve all the problems except
the following ones:
                   45+3=555,56+9=77,56/6=4
Your program should take operator and the two numbers as input from the user
and then return the result'''
#define function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y

#take user input
a=float(input("Enter number 1: "))
b=float(input("enter number 2: "))
c=input("Choose Your Operator [+,-,*,/] : ")

#applying condition

'''This condition for Fault calculation 
            45+3=555,56+9=77,56/6=4'''

if a == 45 and b == 3 and c == '+' or a == 56 and b == 9 and c == '+' or a == 56 and b == 6 and c == '/':
    if  b == 3 and c == '+' :
        print("555")
    elif b == 9 and c == '+' :
        print("77")
    else:
        b == 6 and c == '/'
        print("4")
            
    '''And This condition for Non Fault calculation'''    
else :
    if c == '+' :
        print(add(a,b)) 
    elif c == '-' :
        print(sub(a,b))
    elif c == '*' :
        print(multi(a,b)) 
    elif c == '/' :
        print(div(a,b))
    else:
        print("Please Enter Correct operation")
