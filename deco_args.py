from time import strftime
from functools import wraps

def log_into(fmt="%H:%M:%S"):
    def decorator_log_into(func):
        @wraps(func)
        def execute(*args, **kwargs):
            print(strftime(fmt))
            return func(*args, **kwargs)
        
        return execute
    return decorator_log_into


@log_into(fmt='%H:%M:%S')
def backpackers():
    return 42

@log_into(fmt='%d:%m:%Y')
def hi(name):
    return f'hi {name}'


if __name__ == '__main__':
    print(backpackers())  # imprime 42
    print(backpackers.__name__)  # imprime backpackers
    print(hi('Bob'))  # imprime hi Bob
    print(hi('Alice'))  # imprime hi Alice
    print(hi.__name__)  # imprime hi