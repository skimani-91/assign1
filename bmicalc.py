weight = int(input("What is your weight in KGs? "))
height = float(input("What is your height in meters? "))

h2 = height*height
bmi = round(weight/h2,2)
normalbmi = 19

if bmi < normalbmi :
    print("You are underweight and your BMI is",bmi)
elif ((bmi>= normalbmi) and (bmi <= 25)):
    print("You have normal weight and your BMI is",bmi)
else:
    print("You are overwight and your BMI is",bmi)
    