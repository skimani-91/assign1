year = int(input("What year were you born in? "))

ageYears = 2023 - year
ageMonths = ageYears*12
ageDays = ageMonths*365

print("You are",ageYears,"years old or",ageMonths,"months old")
print("You can also say that you are",ageDays,"days old")