# Exercise 2: Simple Calculator (if/elif/else)
# Write a program that asks the user for:

# Two numbers (float or int).

# An operation (+, -, *, /).

# Then, perform the operation using if/elif/else and print the result.

num1=float(input("Enter the first  number: "))
num2=float(input("Enter the second number: "))


while True:
    cal=input("WHat do you want to do in calculation ( \n1.+ \n2.- \n3.* \n4./ : ")



    if cal=="1":
        print(num1+num2)
        break

    elif cal=="2":
        print(num1-num2)
        break

    elif cal=="3":
        print(num1*num2)
        break

    elif cal=="4":
        print(num1/num2)
        break

    else:
        print("Enter valid operation in calculator")
        continue