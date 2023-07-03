
students = [('Jhon', 'A', 15), ('Sara', 'B', 12), ('Tony', 'C', 10)]

students.sort(key=lambda student: student[2])


def for_name(student):
    return student[0]

print(students)
print(sorted(students, key=for_name))