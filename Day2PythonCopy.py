print("Welcome to the tip calculator.")
bill = float(input("What was th total bill? "))
#tipp means tip percentage 
tipp = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1 
people = float(input("How many people to split the bill? "))
ind_bill = round(bill * tipp / people, 2)
print(f"Each person should pay: ${ind_bill}")