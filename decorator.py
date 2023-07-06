
def fabric_multiplication():
    def multiply(a):
        return a * 2
    return multiply

double = fabric_multiplication()
double2 = fabric_multiplication()

print(double is double2)
print(double(2))
print(double(3))
