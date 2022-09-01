height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}. You are underweight, please eat.")
elif bmi < 25:
    print(f"Your bmi is {bmi}. You are a normal weight, good work.")
elif bmi < 30:
    print(f"Your bmi is {bmi}. You are overweight, work hard to get that down.")
elif bmi < 35:
    print(f"Your bmi is {bmi}. You are obese, your health is in danger now don't eat so much.")
else:
    print(f"Your bmi is {bmi}. You are clinically obese, Please see professional help.")