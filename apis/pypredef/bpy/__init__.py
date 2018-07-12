"""Give access to blender data and utility functions."""


class _default:
    def __init__(self, *args, **kwargs):
        pass

class _wrapper(object):



    class Operator(_default):
        pass

    class Panel(_default):
        pass

    class PropertyGroup(_default):
        pass

    class IntProperty(_default):
        pass

    class BoolProperty(_default):
        pass

app = _wrapper
context = _wrapper
data = _wrapper
ops = _wrapper
path = _wrapper
props = _wrapper
selection_osc = list
types = _wrapper
use_overrides = bool
utils = _wrapper

