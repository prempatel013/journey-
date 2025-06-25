"""
🐍 PYTHON DAY 1 MASTER FILE 🐍
Covers ALL fundamental concepts with:
- Theory explanations
- Practical examples
- Interactive exercises
- Pro tips
"""

# ================ 1. VARIABLES & DATA TYPES ================
print("\n" + "="*40 + "\n📦 VARIABLES & DATA TYPES\n" + "="*40)

"""
🔍 Theory:
Variables are named containers that store data
Python has 4 main data types:
1. int   - whole numbers (42)
2. float - decimals (3.14)
3. str   - text ("Hello")
4. bool  - True/False
"""

# 🛠️ Basic Examples
age = 25                          # int
price = 19.99                     # float
name = "Alice"                    # str
is_student = True                 # bool

# 💡 Pro Tip: Use type() to check variable types
print(f"Type of age: {type(age)}")
print(f"Type of name: {type(name)}")

# 🎯 Exercise: Create variables for:
# - Your favorite number (my_num)
# - Your height in meters (my_height)
# - Your name (my_name)
# - Whether you like Python (likes_python)

# ================ 2. OPERATORS ================
print("\n" + "="*40 + "\n➕ OPERATORS\n" + "="*40)

"""
🔍 Operator Types:
1. Arithmetic: + - * / // % **
2. Comparison: > < == != >= <=
3. Logical: and or not
"""

# 🛠️ Examples
x = 10
y = 3

# Arithmetic
print(f"{x} + {y} = {x + y}")    # Addition
print(f"{x} ** {y} = {x ** y}")  # Exponentiation 

# Comparison
print(f"Is {x} even? {x % 2 == 0}")

# Logical
sunny = True
weekend = False
print(f"Go outside? {sunny and weekend}")

# 🎯 Exercise: Calculate:
# 1. Area of circle (radius = 5)
# 2. Check if 2024 is leap year
#    (divisible by 4 but not 100, or divisible by 400)

# ================ 3. INPUT/OUTPUT ================
print("\n" + "="*40 + "\n🗣️ INPUT/OUTPUT\n" + "="*40)

# 🛠️ Basic I/O
user_name = input("What's your name? ")
print(f"Hello, {user_name}! Welcome to Python.")

# 💡 Pro Tip: input() always returns string!
# Convert for numbers:
age = int(input("How old are you? "))
print(f"In 10 years, you'll be {age + 10}")

# 🎯 Exercise: Create BMI calculator:
# weight_kg = float(input("Weight (kg): "))
# height_m = float(input("Height (m): "))
# bmi = weight_kg / (height_m ** 2)

# ================ 4. TYPE CONVERSION ================
print("\n" + "="*40 + "\n♻️ TYPE CONVERSION\n" + "="*40)

# 🛠️ Examples
num_str = "42"
num_int = int(num_str)   # String to int
pi_str = str(3.14)       # Float to string

# 💡 Pro Tip: Handle conversion errors
try:
    user_age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number!")

# ================ 5. STRING OPERATIONS ================
print("\n" + "="*40 + "\n🔤 STRING OPERATIONS\n" + "="*40)

# 🛠️ Examples
greeting = "hello world"

print(greeting.upper())           # HELLO WORLD
print(greeting.capitalize())      # Hello world
print(len(greeting))              # 11 (including space)
print("world" in greeting)        # True

# 💡 Pro Tip: f-strings (Python 3.6+)
name = "Bob"
print(f"Hello, {name}! You have {len(name)} letters in your name.")

# ================ 🎯 DAY 1 PROJECTS ================
print("\n" + "="*40 + "\n🎯 DAY 1 PROJECTS\n" + "="*40)

# Project 1: Mad Libs Generator
print("\n🎭 Mad Libs Generator")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
print(f"The {adjective} {noun} jumped over the lazy dog!")

# Project 2: Unit Converter
print("\n📏 Unit Converter")
miles = float(input("Enter miles: "))
km = miles * 1.60934
print(f"{miles} miles = {km:.2f} km")  # :.2f rounds to 2 decimals

# ================ 📝 NOTES SECTION ================
"""
📝 My Personal Notes:

[Add your own notes here as you learn]
- Date: [YYYY-MM-DD] 
- Note: [Your observation]

Example:
- 2023-10-01: Learned that // does floor division (drops decimals)
- 2023-10-01: Remember to convert input() for numbers!
"""

# ================ 🚀 WHAT'S NEXT? ================
"""
Tomorrow's Topics:
1. Conditional statements (if/elif/else)
2. Loops (for/while)
3. Lists and tuples

Try these now if you're curious!
"""

print("\n" + "="*40 + "\n🎉 CONGRATS ON COMPLETING DAY 1! 🎉\n" + "="*40)