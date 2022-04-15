print("Welcome to the computer quiz!!")
playing = input("Do you want to play the quiz? Y/N ")
# print(playing)
if playing !='Y':
    print("quitting")
    quit()
print("Okay let's play!! :)")
print("What does CPU stand for ? ")
print("a) Central Programming Unit")
print("b) Central Processing Unit")
print("c) Centre Processor Unit")
answer=input("Enter your choice: ")
if answer.lower()=='b':
    print("Correct!")
else:
    print("Wrong answer!")    
