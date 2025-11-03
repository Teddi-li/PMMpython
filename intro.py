def add(a, b):  return a + b
def sub(a, b):  return a - b
def mul(a, b):  return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot mod by zero.")
    return a % b

def power(a, b):  return a ** b

ops = {"+": add, "-": sub, "*": mul, "/": div, "%": mod, "^": power}

print("=== Function-Based Calculator ===")
while True:
    keeptry = input("Do you want to try a calculation? (Y/N): ").strip().lower()
    if keeptry != "y":
        print("Thanks for using the calculator.")
        break

    print("Available: +  -  *  /  %  ^")
    userinput = input("Which operation? : ").strip()
    if userinput not in ops:
        print("Invalid operation.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    try:
        result = ops[userinput](a, b)
        print(f"{a} {userinput} {b} = {result}")
    except ZeroDivisionError as e:
        print("Error:", e)
