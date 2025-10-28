month = int(input("What is your birth month? "))
day = int(input("What is your birth day? "))
year = int(input("What is your birth year? "))
print("you were born on "+str(month)+"/"+str(day)+"/"+str(year))
if month>12 or day>31 or year>2024:
    print("Error: Invalid date")
elif month==2 and day>29:
    print("Error: Invalid date")
elif month in [4,6,9,11] and day>30:
    print("Error: Invalid date")
else:
    print("Thank you for providing your birth date!")
    age = 2024 - year
    print("You are approximately "+str(age)+" years old.")