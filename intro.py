
import sys

password="mypwd123"
attempts=0
max_attempts=3
while attempts < max_attempts:
    user_input = input("Enter the password: ").strip()
    attempts += 1
    if user_input == password:
        print("welcome!!!")
        break
    else:
        print("Incorrect password. Try again.")

    if attempts == max_attempts:
        print("your account is locked try after 24 hrs.")
        break

