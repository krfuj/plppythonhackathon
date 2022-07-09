# The above code is a career advice program. It asks the user a series of questions and based on the
# answers, it gives the user a career advice.
careers = ['doctor', 'actor', 'teacher', 'engineer' ]
career_advice = ['You should be a doctor', 'You should be a teacher', 'You should be an engineer', 'You should be an actor']
career_questions = ["Do you love biology: ", "Are you involved into sports or acting: ", "Do you have a passion in teaching people: ", "Do you like making stuffs: " ]

print("Enter Yes/No to the questions below")
choiceBio = input(career_questions[0] ).lower()
choiceArts = input(career_questions[1]).lower()
choiceTech = input(career_questions[2]).lower()
choiceEng = input(career_questions[3]).lower()

if choiceBio == 'yes':
    print(f"You should be a {careers[0]}")
elif choiceBio == 'no':
    if choiceArts == 'yes':
        print(f"You should be {careers[1]}")
    elif choiceArts == 'no':
        if choiceTech == 'yes':
            print(f"You should be {careers[2]}")
        elif choiceTech == 'no':
            if choiceEng == 'yes':
                print(f"You should be {careers[3]}")
            elif choiceTech == 'no':
                exit()        
else:
    print("Invalid input")
    
