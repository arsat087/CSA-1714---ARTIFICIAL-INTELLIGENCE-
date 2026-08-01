
m = int(input("Enter number of Missionaries: "))
c = int(input("Enter number of Cannibals: "))

if m == 3 and c == 3:
    steps = [
        (3, 3, "Left"),
        (3, 1, "Right"),
        (3, 2, "Left"),
        (3, 0, "Right"),
        (3, 1, "Left"),
        (1, 1, "Right"),
        (2, 2, "Left"),
        (0, 2, "Right"),
        (0, 3, "Left"),
        (0, 1, "Right"),
        (1, 1, "Left"),
        (0, 0, "Right")
    ]

    print("\nMissionaries  Cannibals  Boat")
    print("--------------------------------")
    for s in steps:
        print(s[0], "\t\t", s[1], "\t\t", s[2])

    print("\nGoal Reached!")

else:
    print("This simple program works only for 3 Missionaries and 3 Cannibals.")
