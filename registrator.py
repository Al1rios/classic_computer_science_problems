
_marked = []

def get_marked():
    return _marked

def to_marked(f):
    _marked.append(f)
    return f
