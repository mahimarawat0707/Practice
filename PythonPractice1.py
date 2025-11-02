#WAP to check if a number by the user is odd or even.
num = int(input("Enter your number: "))
if(num % 2 == 0):
  print("Number is even")
else:
  print("Number is odd")

#WAP to find the greatest of 3 numbers entered by the user.
a = int(input("Write your first number: "))
b = int(input("Write your  second number: "))
c = int(input("Write your third number: "))
if(a > b and a > c):
  print("A is greatest")
elif(b > a and b > c):
  print("B is greatest")
else:
  print("C is greatest")

#WAP to check if the number is multiple of 7 or not.
num = int(input("Write your number: "))
if(num % 7 == 0):
  print("Number is divisible by seven")
else:
  print("Number is not divisible by seven")
