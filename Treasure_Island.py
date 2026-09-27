print("Welcome to the Treasure Island")
print("your mission is to find the treasure")
choice1=input('you\'re at a cross road,where do you want to go .'
               'type "left" or "right".\n').lower()
if choice1=="left":
    choice2=input('You\'re come to a lake.'
                   'There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat .'
                     'Type "swim" to swim across the lake.\n').lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed."
                      "there is a house with a three doors. one red,"
                      " one yellow door and one blue door.\n")
        if choice3=="red":
            print("it's a room full of fire.Game Over")
        elif choice3=="yellow":
            print("you found the treasure. You Win!")
        elif choice3=="blue":
            print("you enter a room of beast. Game Over")
        else:
            print("you choose a door that doesn't exist.Game Over")
    else:
        print("you got attacked by angry trout.Game Over")
else:
        print("you fell in to a hole.Game Over")
