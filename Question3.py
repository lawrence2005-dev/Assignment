# Dictionary containing five students and their marks
students = {
    "Chiko": 75,
    "Jila": 82,
    "Ano": 68,
    "Cory": 91,
    "Lawrence": 79
}

# Display all students and their marks
print("Students and their marks:")

for student, mark in students.items():
    print(student, ":", mark)

# Find the student with the highest mark
highest_student = max(students, key=students.get)
highest_mark = students[highest_student]

print("\nStudent with the highest mark:")
print(highest_student, ":", highest_mark)