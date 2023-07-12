from time import strftime
def log_into(func):
    def execute(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return func(*args, **kwargs)
    return execute


@log_into
def backpackers():
    return 42

@log_into
def hi(name):
    return f'hi {name}'

if __name__ == '__main__':
    print(backpackers())
    print(hi('Bob'))
    print(hi('Alice'))
    print(hi('John'))
   