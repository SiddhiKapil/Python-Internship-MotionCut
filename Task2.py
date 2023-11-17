print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
di = input("Would you like to go 'Left' or 'Right'?")
left_or_right = di.lower()

if left_or_right == 'left':
    sw = input("Would you like to Swim or Wait?")
    swim_or_wait = sw.lower()
    
    if swim_or_wait == 'wait':
        wd = input("Which door would you like to choose between red, yellow, and blue:")
        door = wd.lower()

        if door == 'yellow':
            print("You WIN!")
        elif door == 'red':
            print("Burned by fire. GAME OVER!")
        elif door == 'blue':
            print("Eaten by Beasts. GAME OVER!")
        else:
            print("GAME OVER!")
    else:
        print("Attacked By trout. GAME OVER!")
else:
    print("Fell into a Well. GAME OVER!")
