import pprint
import inspect


def introspection_info(obj):
    info = dict()
    info['type'] = type(obj)
    info['attributes'] = []
    info['methods'] = []
    for key, value in inspect.getmembers(obj):
        if callable(value):
            info['methods'].append(key)
        else:
            info['attributes'].append(key)
    info['module'] = inspect.getmodule(obj).__name__

    return info


class MyClass:
    pass


def func():
    pass


a = MyClass()
b = func
c = int
pprint.pprint(introspection_info(b))
