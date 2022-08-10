'''keypoints :
    1.no of guesses9
    2.print no of guesses left
    3.No of guesses he took to finish
    4.game over'''
n=13
for i in range (0,9):
    a=int(input("Guess The Number Between 0 TO 20\n"))
    j=8-i
    
    if a==n:
        print(f"Congrats Correct Number,[{i}] Guess you take to finish")
        break
    elif a>=0 and a<=5:
        print("You are too far Try again!")
    elif a>=5 and a<=10:
        print("You are little close Try again!")
    elif a>=10 and a<=15:
        print("You are too close Try again!")
    elif a>=15 and a<=20:
        print("You are too far Try again!")
    else:
        a>20
        print("!Enter Correct number!")
    print(f"You have {j} guess left")
    
    if j==0:
        print("Game Over!")
        break
