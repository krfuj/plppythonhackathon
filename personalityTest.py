# Asking the user how many books they have purchased from serendipity so far. Then it is giving them
# points based on how many books they have purchased.
numBook_bought = int(input("How many books have you purchsed from serendipity so far: "))
if numBook_bought == 0:
    print("You have: O points")
elif numBook_bought ==1:
    print("You have: 6")
elif numBook_bought ==2:
    print("You have: 16")
elif numBook_bought ==3:
    print("You have: 32")
elif numBook_bought ==4:
    print("You have: 60")
else:
    print("Thank you for shopping with us")