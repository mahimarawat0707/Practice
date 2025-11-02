#WAP to ask the user to enter names of their 3 favourite movies and store them in a list
movies = []
mov1 = input("Enter a movie name: ")
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3rd movie name: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#WAP to check if a list contains a palindrome of elements
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
  print("Palindrome")
else:
  print("Not Palindrome")

#WAP to count the number of students with the grade "A" in the following tuple
#    ["C", "D", "A", "A", "B", "B", "A"]

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

#Store the above values in a list & sort them from "A" to "D"
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)
