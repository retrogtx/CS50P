# students = ["Hermoine", "Harry", "Ron", "Draco"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=": ")
