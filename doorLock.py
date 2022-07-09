import re
from datetime import datetime

def door_lock():
    """
    It takes a command from the user, and if the command is "open", it opens the door, if the command is
    "close", it closes the door, if the command is "help", it prints the help message, and if the
    command is "quit", it quits the program
    """
    command = ""
    openned = False
    while True:
        command = input(": ").lower()
        if command == 'open':
            if openned:
                print("The door is already open")
            else:
                openned = True
                now = datetime.now()
                print(f"Door last open at {now}")
                print("The door is now open")
        elif command == 'close':
            if not openned:
                print("The door is already locked")
            else:
                openned = False
                now = datetime.now()
                print(f"Door last locked at {now}")
                print("The door is now locked")
                
        elif command == "help":
            print("""
            open - to open the door
            close - to close the door
            quit - to quit
            """)
        elif command == 'quit':
            print("Quiting this process")
            break
        else:
            print("Invalid input")



def set_validatePwd():
    """
    It asks the user to enter a password, and if the password is less than 8 characters, doesn't have a
    number, or doesn't have a capital letter, it tells the user what they need to do to fix it. 
    
    If the password is fine, it breaks out of the loop.
    """
    global password1
    password1 = ''

    while True:
        password1 = input("Enter a password: ")
        if len(password1) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password1) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password1) is None: 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break
    

set_validatePwd()
# Asking the user to enter a password, and if the password is correct, it will open the door, if the
# password is wrong, it will tell the user that the password is wrong, and it will tell the user how
# many tries they have left.
tries = 3
while (tries > 0):
    password = input("Enter Password to login: ")
    if password == password1:
        print("login succesful")
        door_lock()
        tries = 0
    else:
        tries -=1
        print("Wrong password try again,you have {tries} tries left")

        
            
        

