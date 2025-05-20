import random

print("🎯 Welcome to our game!")
print("I'm thinking of a number between 1 to 100.")
print("Let's see how many attempts you take to guess it!")

secret = random.randint(1, 100)
guesses = 0

while True:
    try:
        user_input = input("🔢 What is your guess? ")
        guess = int(user_input)
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    guesses += 1

    if guess < secret:
        print("🔼 Try a higher number.")
    elif guess > secret:
        print("🔽 Try a lower number.")
    else:
        print(f"✅ Correct! You guessed it in {guesses} attempts. 🎉")
        break
