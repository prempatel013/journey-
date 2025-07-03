# Exercise 8: FizzBuzz (Advanced if/else & loop)
# Print numbers from 1 to 20, but:

# If a number is divisible by 3, print "Fizz".

# If divisible by 5, print "Buzz".

# If divisible by both, print "FizzBuzz".

for i in range(1,21):
    
    if i % 3 == 0:
        print(f"{i} is divisible by 3 : Fizz ")
    elif i%5 ==0:
        print(f"{i} is divisible by 5: Buzz")
        
    elif  i % 3 == 0 and i%5 ==0:
        print(f"{i} is divisible by both: FizzBuzz")
    else:
        print(f"{i}")