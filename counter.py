_counter = 0
def counter_factory():
    def count():
        global _counter
        _counter += 1
        return _counter
    return count

counter = counter_factory()
counter2 = counter_factory()

print(counter())
print(counter())
print(counter())
print(counter2())
print(counter2())