# def memoize(f):
#     """ Memoization decorator for a function taking one or more arguments. """
#     class MemoDict(dict):
#         def __getitem__(self, *key):
#             return dict.__getitem__(self, key)
#
#         def __missing__(self, key):
#             ret = self[key] = f(*key)
#             return ret
#
#     return MemoDict().__getitem__

from itertools import tee
from types import GeneratorType

Tee = tee([], 1)[0].__class__


def memoized(f):
    cache = {}

    def ret(*args):
        if args not in cache:
            cache[args] = f(*args)
        if isinstance(cache[args], (GeneratorType, Tee)):
            # the original can't be used any more,
            # so we need to change the cache as well
            cache[args], r = tee(cache[args])
            return r
        return cache[args]

    return ret
