num1 = float(input("Enter the first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter the second number: "))


if op == "-":
    cal = num1 - num2 
    print(f"{num1} - {num2} = {cal}")
elif op == "+":
    cal = num1 + num2 
    print(f"{num1} + {num2} = {cal}")
elif op == "*":
    cal = num1 * num2 
    print(f"{num1} * {num2} = {cal}")
elif op == "/":
    cal = num1 / num2 
    print(f"{num1} / {num2} = {cal}")
else:
    print("invalid operator")
