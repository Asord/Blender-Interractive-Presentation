class Singloton(object):

    instance = None
    _ClassName = None  # OVERRIDE

    def __new__(cls, *args):
        if cls.instance is None:
            cls.instance = cls._ClassName(*args)
        return cls.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)

"""
class [name](Singloton):
    class __[name](object):
        ...
    
    _ClassName = __[name]
"""