# This is a program that calculates the amount of paint needed to paint a wall.
wall_space = 115
galon_paint = 1
labour_hourlyCost = 20


userWall_space = int(input("Enter a your wallspace: "))
needed_gallonPaint = userWall_space / 115
hours_required = needed_gallonPaint * 8
Overal_LabourCost = hours_required * labour_hourlyCost

print(f"For {userWall_space} square foot will need {needed_gallonPaint} gallons of paint, {hours_required} hours to complete, {Overal_LabourCost} for labour with cost")

