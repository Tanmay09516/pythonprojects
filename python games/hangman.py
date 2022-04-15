import random 
import string
words =['cat','dog','animal','madlibs','zebra','horse','donkey']
def get_word(words):
    word= random.choice(words)
    while '_' in word or '-' in word or " " in word:
        word= random.choice(words)
    return word.upper()
def hangman():
    lives =7
    word = get_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabets = set(string.ascii_uppercase)
    while len(word_letters)>0 or lives>0:
        print(lives)
        print ("You have used these letters :"," ".join(used_letters))
        word_list=[letter if letter in used_letters else "-" for letter in word]
        print("Current word : "," ".join(word_list))
        user_input = input("Guess a letter: ").upper()
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives=lives-1
                if lives==0:
                    break
                print("WRONG!!! Guess again")
        elif user_input in used_letters:
            print("You have already used this letter. Choose a diffrent one.")
        else:
            print("Invalid Entry")
    if lives==0:
        print("OOPS!! You Died")
    else:
        print(f"CONGRATULATIONS!!! You won\n The word was {word}")
hangman()