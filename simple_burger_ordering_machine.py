'''
print("Hello! Welcome to Python Burger Deliveries!")

small_price = 15
medium_price = 20
large_price = 25
extra_cheese_price = 1

sauce_small_price = 2
sauce_medium_and_large_price = 3
size = input("What size of burger do you want? S, M, or L: ")

if size == 'S' :
    sauce = input(("Do you want special sauce? Y or N: "))
    if sauce == 'Y':
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = small_price + sauce_small_price + extra_cheese_price 
        else :
            total = small_price + sauce_small_price
    else :
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = small_price + extra_cheese_price
        else :
            total = small_price
elif size == 'M' :
    sauce = input("Do you want special sauce? Y or N: ")
    if sauce == 'Y':
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = medium_price + sauce_medium_and_large_price + extra_cheese_price 
        else :
            total = medium_price + sauce_medium_and_large_price
    else :
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = medium_price + extra_cheese_price
        else :
            total = medium_price

else:
    sauce = input(("Do you want special sauce? Y or N: "))
    if sauce == 'Y':
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = large_price + sauce_medium_and_large_price + extra_cheese_price 
        else :
            total = large_price + sauce_medium_and_large_price
    else :
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == 'Y':
            total = large_price + extra_cheese_price
        else :
            total = large_price



print ("Your final bill is : " + "$" + str(total))
'''


# Corrected codes to reduce redundancy and improve readability
print("Hello! Welcome to Python Burger Deliveries!")

# Prices
small_price = 15
medium_price = 20
large_price = 25
extra_cheese_price = 1
sauce_small_price = 2
sauce_medium_and_large_price = 3

# Get size input
size = input("What size of burger do you want? S, M, or L: ").upper()

# Initialize price variable
total = 0

# Set base price based on size
if size == 'S':
    total = small_price
    sauce_price = sauce_small_price
elif size == 'M':
    total = medium_price
    sauce_price = sauce_medium_and_large_price
elif size == 'L':
    total = large_price
    sauce_price = sauce_medium_and_large_price
else:
    print("Invalid size selected. Please choose S, M, or L.")
    exit()

# Get sauce and extra cheese input
sauce = input("Do you want special sauce? Y or N: ").upper()
if sauce == 'Y':
    total += sauce_price

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == 'Y':
    total += extra_cheese_price

# Print final bill
print(f"Your final bill is: ${total}")
