from registrator import get_marked, to_marked


def first():
    pass

first = to_marked(first)

@to_marked
def secund():
    pass



if __name__ == '__main__':
    for f in get_marked():
        print(f.__name__)
        first()
        secund