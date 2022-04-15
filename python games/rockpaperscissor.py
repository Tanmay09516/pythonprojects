from random import *
def play():
    print("Welcome to Rock Paper Scissors")
    loop=0
    while True:
        user=input("Make your choice, 'r' for rock, 's' for scissors, 'p' for paper: ")
        while True:
            if user=='r' or 's' or 't':
                break
            else:
                user= input("Invalid input! Try again! ")
                continue
        computer=choice(['r','p','s'])
        print(f"Your choice: {user}")
        print(f"Computer's choice {computer}")
        if user==computer:
            y=int(input("it's a tie. Press 1 to try again and 0 to end "))
            while True:
                if y==1:
                    loop=1
                    break
                elif y==0:
                    loop=0
                    break
                else:
                    x = int(input("invalid input try again! "))
                    continue
        else:
            if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p'and computer=='r'):
                x = int(input("You won!! Press 2 to try again and 0 to end "))
                while True:
                    #x = int(input("You won!! Press 2 to try again and 0 to end"))
                    if x==2:
                        loop=1
                        break
                    elif x==0:
                        loop=0
                        break
                    else:
                        x = int(input("invalid input try again!"))
                        continue
            else:
                x=int(input("Computer won!!Press 2 to try again and 0 to end"))
                while True:
                    # x = int(input("Computer won!!Press 2 to try again and 0 to end"))
                    if x==2:
                        loop=1
                        break
                    elif x==0:
                        loop=0
                        break
                    else:
                        x = int(input("invalid input try again!"))
                        continue
        if loop==0:
            break
play()
#r>s,s>p,p>r