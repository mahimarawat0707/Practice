# Filter numbers greater than 50 from a list

numbers = [10, 67, 45, 89, 23, 90, 4]
greater_than_50 = list(filter(lambda x: x > 50, numbers))

print("Numbers > 50:", greater_than_50)
