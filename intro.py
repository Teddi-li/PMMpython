name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)
weight = input("What is your weight in kg? ")
weight = float(weight)
height = input("What is your height in cm? ")
height = float(height) / 100  
mbi = (weight / (height ** 2)) 
def mbi_category(mbi):
    if mbi < 18.5:
        return "underweight"
    elif 18.5 <= mbi < 24.9:
        return "normal weight"
    elif 25 <= mbi < 29.9:
        return "overweight"
    else:
        return "dangerously overweight"
print("Hello,", name + "! You are", age, "years old.")
print(f"Your  MBI is {mbi:.1f} you are {mbi_category(mbi)}")