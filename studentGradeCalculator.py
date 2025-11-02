def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def save_record(name, marks, grade):
    with open("student_records.txt", "a") as f:
        f.write(f"{name} - {marks} - Grade: {grade}\n")

while True:
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))
    grade = calculate_grade(marks)

    print(f"✅ {name} scored {marks} and received grade: {grade}")

    save_record(name, marks, grade)
    if input("Add another? (y/n): ").lower() != 'y':
        break
