BillAmount = int(input("Hello, what is your bill today? "))
tipPercent = int(input("What percent(10,12 or 15) will be assigned to the tip? "))
peopleAmount = int(input("How many people will pay the bill? "))

tip = (BillAmount/100)* tipPercent
totalBill = tip + BillAmount
personPay = float(totalBill/peopleAmount)
personPay = round(personPay,2)

print("The amount that each person will pay is",personPay)