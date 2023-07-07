
def multiplication_factory():
    def multiply(a):
        return a * 2
    return multiply

double = multiplication_factory()
double2 = multiplication_factory()

print(double is double2)
print(double(2))
print(double(3))
