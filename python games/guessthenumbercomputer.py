from random import *
def guess():
    print("Welcome to guess the number: ")
    low=int(input("Enter the lower limit of the guessing game: "))
    high=int(input("Enter the higher limit of the guessing game: "))
    # low=1 
    # high=100
    response=''
    while response!='c':
        guess=randint(low,high)
        response=input(f"Is {guess} too high(H), too low(L) or correct(C)? ")
        if response=='h':
            high=guess-1
        elif response=='l':
            low=guess-1
    print(f"Yay! The computer guessed your number,{guess}.")
guess()
