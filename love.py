import time

def heart():
    heart_shape = [
        "  **   **  ",
        " ****** **** ",
        "*************",
        " *********** ",
        "  *********  ",
        "    *****    ",
        "      *      "
    ]
    for line in heart_shape:
        print(line)
        time.sleep(0.2)

print("💌 Welcome to the Valentine's Day Program 💌")
time.sleep(1)

name = input("Enter your Valentine's name: ")

print("\nCreating something special for you...\n")
time.sleep(1)

heart()

print(f"\n💖 Happy Valentine's Day, {name}! 💖")
print("You are loved, appreciated, and totally amazing ✨")
print("May your day be full of smiles, chocolates 🍫, and good vibes 🌸")
