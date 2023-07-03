
"""_summary_

>>> def hi():
...     print('hi')
...
>>> execute(hi)
hi
>>> execute(hi, 2)
hi
hi
>>> def hello_world():
...     print('hello world')
...
>>> execute(hello_world, 3)
hello world
hello world
hello world

"""

def execute(func, n=1):
    for _ in range(n):
        func()

