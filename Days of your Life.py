age = int(input("What is your current age? "))
death = 90
dleft_age = (death * 365) - (age * 365) 
wleft_age = (death * 52) - (age * 52) 
mleft_age = (death * 12) - (age * 12) 
print (f"You have {dleft_age} days, {wleft_age} weeks, and {mleft_age} months left.")