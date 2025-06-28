# Project 1: Smart Temperature Advisor 🌡️
# Concepts Used: Conditionals, user input

temp = float(input("Enter current temperature (°C): "))

if temp > 30:
    print("It's hot! Stay hydrated.")
elif 20 <= temp <= 30:
    print("Nice weather!")
else:
    print("It's cold. Bring a jacket.")