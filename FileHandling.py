with open("data.txt", "w") as f:
    f.write("Hello, Python!")

with open("data.txt", "r") as f:
    print(f.read())
