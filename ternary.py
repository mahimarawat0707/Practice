food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

food = input("food : ")
print ("Sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#clever if
age= int(input("age : "))
vote = ("yes", "no") [age<=18]
print(vote)
