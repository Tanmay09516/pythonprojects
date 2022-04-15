from random import *
def guess():
    print("Welcome to Guess The Number!!!")
    guess= int(0)
    random_number=int(randint(1,99))
    while guess!=random_number:
        guess=int(input("Enter your guess: "))
        if guess<random_number:
            print("Your guess is lesser than the number!")
        elif guess>random_number:
            print("Your guess is greater than the number!")
    print(f"Congrats! the number was {random_number} !!")
guess()