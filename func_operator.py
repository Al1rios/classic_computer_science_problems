import operator

students = [('Jhon', 'A', 15), ('Sara', 'B', 12), ('Tony', 'C', 10)]


print([ name for name in students if name[2] >= 12])

def filter_grades_above_twelve(student):
    _, _, grade=student
    return grade >= 12

def extract_name(student):
    return operator.itemgetter(0)

print(list(map(extract_name(students), filter(filter_grades_above_twelve,students))))

print(list(map(operator.itemgetter(0), filter(filter_grades_above_twelve,students))))
