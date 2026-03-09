
import random

while True:

    length = int(input("Enter password length: "))

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour Generated Secure Password is:", password)

    again = input("\nDo you want another password? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye! 👋")
        break