info = {
  "key" : "value",
  "name" : "Mahima",
  "learning" : "python",
  "age" : 18,
  "is_adult" : True,
  "marks" : 99.9
}
print(type(info))
print(info["age"])

info["name"] = "Mahima Rawat" #it is mutable
print(info)

null_dict = {} #empty dictionary
print(null_dict)

#NESTED DICTIONARY
student = {
  "name" : "Mayank",
  "subjects" : ["physics", "Chemestry", "Maths"], #list
  "marks" : {
    "Physics" : 99.9,
    "Chemestry" : 98.99,
    "maths" : 99.8
  }
}
print(student["marks"]["Chemestry"])
print(student)

print(student.keys()) #return all keys
print(student.values()) #return all values
print(student.items()) #return all (key, val) pairs as tuples
print(student.get("marks")) #return the key according to value
student.update {"surname" : "Rawat"}) #insert the specified items to the dictionary
print(student)
