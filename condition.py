marks = int(input("Enter your marks: "))
if(marks >= 90):
  grade = "A" #indentation- the gaping
elif(marks >= 80 and marks < 90):
  grade = "B"
elif(marks >= 70 and marks < 80):
  grade = "C"
else:
  grade = "D"

print("Grade of the student ->", grade)

#nesting
age = 85
if(age >= 18):
  if(age >= 80):
    print("cannot drive")
  else:
    print("can drive")
else:
  print("cannot drive")
