
# Exercise 6: Grade Classifier
# Ask the user for their exam score (0-100) and classify it:

# A (90-100)

# B (80-89)

# C (70-79)

# D (60-69)

# F (<60)





grade=int(input("Enter your grade: "))

if grade>=90:
   print('you got A 🙌')
elif grade>=80:
   print('you got B grade')
elif grade>=70:
   print('you got C grade')
elif grade>=60:
   print('you got D grade')

else:
   print('you got F grade')