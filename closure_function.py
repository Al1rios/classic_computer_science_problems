# multiplication function : multiplicand * multiplier


def multiplication_factory(multiplier):
    def multiply(a):
        return a * multiplier
    return multiply

double = multiplication_factory(2)
triple = multiplication_factory(3)

print(double(2))
print(triple(4))