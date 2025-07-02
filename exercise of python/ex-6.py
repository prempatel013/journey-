# Exercise 6: Grade Classifier
# Ask the user for their exam score (0-100) and classify it:

# A (90-100)

# B (80-89)

# C (70-79)

# D (60-69)

# F (<60)

grade=input("Enter your grade: ")

if grade>=90:
   print('you got A')
elif grade>=80:
   print('B')
elif grade>=70:
   print('C')
elif grade>=60:
   print('D')
elif grade>60:
   print('F')
