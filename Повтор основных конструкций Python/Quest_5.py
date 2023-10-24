import functools
import json

def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = json.dumps(func(*args))
        return result
    return wrapper