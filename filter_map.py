students = [('Jhon', 'A', 15), ('Sara', 'B', 12), ('Tony', 'C', 10)]


print([ name for name in students if name[2] >= 12])

def filter_grades_above_twelve(student):
    _, _, grade=student
    return grade >= 12

print(list(filter(filter_grades_above_twelve, students)))



# students.sort(key=lambda student: student[2])


# def for_name(student):
#     return student[0]

# print(students)
# print(sorted(students, key=for_name))