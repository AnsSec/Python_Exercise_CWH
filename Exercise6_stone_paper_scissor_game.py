# Exercise 6: Game Development: stone paper scissor
import random
c=0
p=0
t=0
print('\t\t\tWelcome To \n\t\t<!stone<|>paper<|>scissor!>')
for i in range (1,10+1):
    p1=p
    c1=c
    t1=t
    sps=[1,2,3]
    i=i+1
    num=random.randint(1,3)
    comp=num
    player=int(input("\nIt's Your turn | 1:Stone | 2:Paper | 3:Scissor| :"))
    print(f'{11-i} left out of 10')
    if comp==player:               
        t=t+1
    elif sps.count(player)>0:
        if comp==1:
            if player==2:
                p=p+1
            else:
                player==3
                c=c+1
        elif comp==2:
            if player==3:
                p=p+1
            else:
                player==1
                c=c+1
        elif comp==3:
            if player==1:
                p=p+1
            else:
                c=c+1
    else:
        print('choose correct option')
if c1>p1:
    print('Computer Win')
else:
    print('You Win')
print(f'\n\t\t <|>Score card<|>\n\n<|You     : {p1}|>\n<|Computer: {c1}|>\n<|Draw    : {t1}|>')
