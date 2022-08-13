#Exercise 4 Patteren print
num=int(input("Enter a number :"))
c=int(input("choose 1 or 0 :"))
if 1==c:
    for i in range(num):
        print("*" * i)
elif 0==c:
    for i in range(num):
        i=num-i
        print("*" * i)
else:
    print("Enter Correct option")
