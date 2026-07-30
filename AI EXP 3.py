jug1 = 4
jug2 = 3

x = 0
y = 0

print("Steps:")

while True:
    print("Jug1 =", x, "Jug2 =", y)

    if x == 2:
        print("Goal Reached!")
        break

    if x == 0:
        x = jug1              
    elif y == jug2:
        y = 0                
    else:
        transfer = min(x, jug2 - y)
        x = x - transfer
        y = y + transfer
