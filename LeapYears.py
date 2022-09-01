year = int(input("which year would you like to check? "))

def leap_year():
    print(f"{year} is a leap year.")
def nleap_year():
    print(f"{year} is not a leap year.")

if year % 400 == 0:
    leap_year()
elif year % 100 == 0:
    nleap_year()
elif year % 4 == 0:
    leap_year()
else:
    nleap_year()