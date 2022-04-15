pwd=input("Enter the password")
def view():
    with open('passwords.txt','r') as r:
        for line in r.readlines():
            data=line.rstrip()
            plat,user,passw=data.split('|')
            print("Platform: "+plat+'\n'+"Username: "+user+'\n'+"Password: "+passw+'\n')
def add():
    platform=input("Enter the platform you are adding the password of: ")
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    with open('passwords.txt', 'a') as f:
        f.write(platform+" | "+username+" | "+password+'\n')
while True:
    mode=input("Would you like to add a password or view the saved passwords? Enter view to view, add to add passwords and q to quit: ")
    if mode=='q':
        quit()
    if mode.lower()=='add':
        #print()
        add()
    elif mode.lower()=='view':
        view()
        pass
    else:
        print("invalid input try again")
        continue
