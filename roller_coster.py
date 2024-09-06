name = input("Enter your name : ")
print("Hello, " + name + "!")

height = int(input("Enter your height (cm) : "))

if height >= 120 :
    print("You can ride the roller coster!")
    age = int(input("Enter your age : "))
    if age <= 12 :
        print("Your ticket price is RM5")
    elif age >= 12 and age <= 18  :
        print("Your ticket price is RM7")
    elif age > 18 and age < 45:
        print("Your ticket price is RM12.") 
    elif age < 56 :
        print("Have a free ride on us!")
    else :
        print("Your age is out of the allowed range.")
else :
    print("Sorry. You need to be more than 120cm. You can't ride the roller coster!")