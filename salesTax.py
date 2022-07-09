# This is a program that calculates the amount of paint needed to paint a wall.
wall_space = 115
galon_paint = 1
labour_hourlyCost = 20


userWall_space = int(input("Enter a your wallspace: "))
price_paint = int(input("Enter price of paint per galon: "))
needed_gallonPaint = userWall_space / 115
cost_paint = needed_gallonPaint * price_paint
hours_required = needed_gallonPaint * 8
Overal_LabourCost = hours_required * labour_hourlyCost
total_cost = cost_paint + Overal_LabourCost

print(f"For {userWall_space} square foot will need {needed_gallonPaint} gallons of paint, {hours_required} hours to complete, the cost of paint being ksh.{cost_paint}. The labour cost will stand at {Overal_LabourCost} for labour with cost making the overrall cost of the paint job be ksh.{total_cost}")

