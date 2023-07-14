from time import strftime
from functools import wraps

def log_into(func):
    @wraps(func)
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
    print(backpackers())  # imprime 42
    print(backpackers.__name__)  # imprime backpackers
    print(hi('Bob'))  # imprime hi Bob
    print(hi('Alice'))  # imprime hi Alice
    print(hi.__name__)  # imprime hi