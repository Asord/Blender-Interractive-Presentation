class _SingletonWrapper:
    """
    A singleton wrapper class. Its instances will be created
    for each decorated classes.
    """

    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance

def singleton(cls):
    """
    A singleton decorator. Returns a wrapper objects. A call on that object
    returns a single instance object of decorated class. Use the __wrapped__
    attribute to access decorated class directly in unit tests
    """
    return _SingletonWrapper(cls)

"""
The simplest way will be to create a decorator that store all singleton instances in a list,
but it may not work with some tools like unit test suit, so we docrate the singleton classes with
a singleton object 
"""