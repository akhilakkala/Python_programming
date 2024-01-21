year = int(input("Enter any Year : "))

if (year%400==0) or (year%100!=0  and year%4==0):
    print(f"The year that you have entered {year} is a leap year")
else:
    print(f"The year that you have entered {year} is not a leap year")

