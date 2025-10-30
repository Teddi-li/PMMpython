name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)
weight = input("What is your weight in kg? ")
weight = float(weight)
height = input("What is your height in cm? ")
height = float(height) / 100  
mbi = (weight / (height ** 2)) 
normal_weight_mbi = 24.9
under_weight_mbi = 18.5
over_weight_mbi = 29.9
def mbi_category(mbi):
    if mbi < under_weight_mbi:
        return "underweight"
    elif under_weight_mbi <= mbi < normal_weight_mbi:
        return "normal weight"
    elif normal_weight_mbi <= mbi < over_weight_mbi:
        return "overweight"
    else:
        return "dangerously overweight"
print("Hello,", name + "! You are", age, "years old.")
print(f"Your  MBI is {mbi:.1f} you are {mbi_category(mbi)}")