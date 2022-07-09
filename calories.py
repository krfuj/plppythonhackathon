# Asking the user to input the amount of fat and carbohydrates they have consumed today in grams. Then
# it is calculating the calories in fats and carbohydrates. Finally, it is printing the calories in
# fats and carbohydrates.
fats = int(input("Please enter the amout of fat you have consumed today in grams: "))
carbohydratess = int(input("Please enter the amout of carbohydrates you have consumed today in grams: "))

calo_Fats = fats * 9
calo_Carbs = carbohydratess * 4

print(f"The calories in you've gianed is {calo_Fats} and for taking carbohydrates is {calo_Carbs} ")