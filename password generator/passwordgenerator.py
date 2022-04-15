from random import *
from string import ascii_lowercase, ascii_uppercase
import string
#smallchar 2 lists
s1=string.ascii_lowercase
s11=[]
s11.extend(list(s1))
s11=choice(s11)
s2=string.ascii_lowercase
s22=[]
s22.extend(list(s2))
s22=choice(s22)
#bigchar 2 lists
b1=string.ascii_uppercase
b11=[]
b11.extend(list(b1))
b11=choice(b11)
b2=string.ascii_uppercase
b22=[]
b22.extend(list(b2))
b22=choice(b22)
#2 lists for symbols
symbol1=choice(['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<','>','.','?','/'])
symbol2=choice(['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<','>','.','?','/'])
#2 lists for numbers
number1=choice(['1','2','3','4','5','6','7','8','9','0'])
number2=choice(['1','2','3','4','5','6','7','8','9','0'])

#making a list to use random shuffle
list=[symbol1,symbol2,number1,number2,s22,s11,b11,b22]
shuffle(list)
#printing the list as a string
for x in range(len(list)):
    print(list[x],end="")
