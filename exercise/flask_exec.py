
"""
>>> app = Flask()
>>> set(app.routes)
set()
>>> @app.route('/')
... def root():
...     return 'root'
...
>>> set(app.routes)
{'/'}
>>> root()
'root'
>>> app.execute('/')
'root'
>>> @app.route('/name')
... def name(user):
...     return f'Name: {user}'
...
>>> list(app.routes)
['/', '/name']
>>> name('python')
'Name: python'
>>> app.execute('/name', 'Pro')
'Name: Pro'
>>> app.execute('/not_found')
404

"""

class Flask:
    def __init__(self):
        self.routes = dict()

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    
    def execute(self, path, *args, **kwargs):
        if path not in self.routes:
            return 404
        # func = self.routes.get(path)
        func = self.routes[path]
        return func(*args, **kwargs)