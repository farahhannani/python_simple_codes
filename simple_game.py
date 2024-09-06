print("Welcome to the game!")

# Define function 1 for monster room
def monster_room():
    try:
        x = int(input("Choose 1 or 2: "))
        if x == 1:
            diamond_room()
        elif x == 2:
            game_over()
        else:
            print("Invalid choice! Try again.")
            monster_room()
    except ValueError:
        print("Invalid input! Please enter a number.")
        monster_room()

# Define function 2 for bear room
def bear_room():
    try:
        y = int(input("Choose 1 or 2: "))
        if y == 2:
            diamond_room()
        elif y == 1:
            game_over()
        else:
            print("Invalid choice! Try again.")
            bear_room()
    except ValueError:
        print("Invalid input! Please enter a number.")
        bear_room()

def diamond_room():
    try:
        a = int(input("Choose 1 or 2: "))
        if a == 2:
            print("You Win!")
        elif a == 1:
            game_over()
        else:
            print("Invalid choice! Try again.")
            diamond_room()
    except ValueError:
        print("Invalid input! Please enter a number.")
        diamond_room()

def game_over():
    print("Game Over!")


# Main game
input1 = input("Choose Left (L) or Right (R): ").strip().upper()

if input1 == 'R':
    monster_room()
elif input1 == 'L':
    bear_room()
else:
    print("Invalid choice! Please choose L or R.")
