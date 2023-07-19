from time import strftime
from decorator import decorator


@decorator
def log_into(func, fmt="%H:%M:%S", *args, **kwargs):
    print(strftime(fmt))
    return func(*args, **kwargs)
      



@log_into
def backpackers():
    return 42

@log_into(fmt='%d:%m:%Y')
def hi(name):
    return f'hi {name}'


if __name__ == '__main__':
    # print(getfullargspec(backpackers))
    print(backpackers())  # imprime 42
    print(backpackers.__name__)  # imprime backpackers
    print(hi('Bob'))  # imprime hi Bob
    print(hi('Alice'))  # imprime hi Alice
    print(hi.__name__)  # imprime hi