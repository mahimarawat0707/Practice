import random

choices = ["r", "p", "s"]
names = {"r": "rock", "p": "paper", "s": "scissor"}

score = 100

def game():
    global score

    print("Welcome to Rock-Paper-Scissors! 🔥")

    while True:
        your_choice = input("Enter rock (r), paper (p), or scissor (s): ").lower()
        if your_choice not in choices:
            print("❌ Invalid input! Please enter 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(choices)
        print(f"\nYou chose -> {names[your_choice]}")
        print(f"Computer chose -> {names[computer_choice]}\n")

        result = (your_choice, computer_choice)
        winning = [("r", "s"), ("s", "p"), ("p", "r")]

        if your_choice == computer_choice:
            print("⚖️ It's a tie!")
        elif result in winning:
            print("✅ You win!")
            score += 10
        else:
            print("❌ You lose!")
            score -= 10

        print(f"Your current score: {score}")

        # Ask to continue
        while True:
            cont = input("\nPress Enter to continue, or type 'n' to quit: ").lower()
            if cont == "n":
                print("\nThanks for playing! 🙌")
                if score > 100:
                    print(f"🔥 Well played! Final score: {score}")
                elif score < 100:
                    print(f"Not bad, try again! Final score: {score}")
                else:
                    print(f"Final score: {score}")
                return
            elif cont == "":
                break
            else:
                print("❗ Invalid input. Press Enter to continue, or type 'n' to quit.")

game()
