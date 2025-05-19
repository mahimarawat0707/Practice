#Print number from 1 to 100.
i = 1
while i <= 100:
  print(i)
  i += 1

#Print nmber from 100 to 1
i = 100
while i >= 1:
  print(i)
  i -= 1

#Print the multiplication table of n
n = int(input("Enter a number"))
i = 1
while i <= 10:
  print(n, "*", i, "=", n*i)
  i += 1

#Print the element of the following list using a loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
  print(nums[idx])
  idx += 1

#Search for a number x in this tuple using loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
  if(nums[i] == x):
    print("Fount at idx", i)
  else:
    print("FINDING...")
  i += 1

  
