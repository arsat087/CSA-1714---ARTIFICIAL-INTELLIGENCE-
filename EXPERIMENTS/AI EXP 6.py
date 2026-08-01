
left = "dirty"
right = "dirty"
location = "left"

print("Initial State:")
print("Left Room :", left)
print("Right Room:", right)
print("Vacuum Location:", location)

print("\nSteps:")

while left == "dirty" or right == "dirty":

    if location == "left":
        if left == "dirty":
            print("Vacuum is in Left Room -> Cleaning Left Room")
            left = "clean"
        else:
            print("Left Room is Clean -> Moving to Right Room")
            location = "right"

    elif location == "right":
        if right == "dirty":
            print("Vacuum is in Right Room -> Cleaning Right Room")
            right = "clean"
        else:
            print("Right Room is Clean -> Moving to Left Room")
            location = "left"

print("\nGoal Reached!")
print("Left Room :", left)
print("Right Room:", right)
