height = float(input("Enter your height (m) : "))
weight = float(input("Enter your weight (kg) : "))

bmi = weight / (height*height)
print("Your BMI is : ", round(bmi,2))


if bmi < 18.5 : 
    print("Underweight")
elif bmi < 25 :
    print("Normal")
elif bmi < 30 :
    print ("Slightly overweight")
elif bmi < 35 :
    print("Obese")
else :
    print("Clinically obese")