marks = [94.4,  87.5,  95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1]) 

#string are immutable (which cannot change) and list are mutable
student = ["karan", 67.8, "Delhi"]
print(student)
print(student[0])
student[0] = "arjun" #it is mutable
print(student)

#slicing
marks = [94.4,  87.5,  95.2, 66.4, 45.1] #last index is not counted
print(marks[1:4]) # like here we wrote 1:4 but it will only take value of 1, 2, 3 only
print(marks[-3:-1])

"""List Methods"""
list = [2, 1, 3]
list.append(4) #adds one element at the end [2,1,3,4]
print(list)

list.reverse() #reverses list
print(list)

list.sort() #sort it in ascending order
print(list)

list.sort(reverse=True) #sort in descending order
print(list)

list.insert(1, 5)
print(list) #insert element at index 

list1 =[2, 1, 3, 1]
list1.remove(1) #remove the first occurence of element
list1.pop(2) #remove the idx
print(list1)
