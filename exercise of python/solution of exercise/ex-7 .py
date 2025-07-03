
# Exercise 7: Sum of Numbers (Loop Practice)
# Write a program that:

# Asks the user for a number n.

# Calculates the sum of all numbers from 1 to n using a loop.

number=int(input("Enter a number: "))
total=0

for i in range(1,number+1):
    total+=i

print(f"the sum of {number} from 1 to {number} is: {total} ")
