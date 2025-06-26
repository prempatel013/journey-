import random

print("\n" + "="*50 + "\n🎮 NUMBER GUESSING GAME\n" + "="*50)

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"Guess the secret number (1-100). You have {max_attempts} tries!")

while attempts < max_attempts:
    try:
        guess = int(input("\nYour guess: "))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break
        elif guess < secret:
            print("⬆️ Higher!")
        else:
            print("⬇️ Lower!")
            
        print(f"Attempts left: {max_attempts - attempts}")
        
    except ValueError:
        print("⚠️ Please enter a valid number!")

else:
    print(f"\nGame over! The number was {secret}")

# Add-ons to try later:
# 1. Add difficulty levels (changes number range)
# 2. Track high scores