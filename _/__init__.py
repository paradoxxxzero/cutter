# -*- coding: utf-8 -*-
from pprint import pprint


class EllipsisGetter(object):
    def __getitem__(self, key):
        return key

ellipsis = EllipsisGetter()[...]


is_string = lambda s: (
    isinstance(s, bytes) or
    isinstance(s, str))

is_iterable = lambda i: (
    hasattr(i, '__iter__') and not
    isinstance(i, dict) and not
    is_string(i))


def flatten(iterable):
    return [
        item
        for subiterable in iterable
        for item in flatten(subiterable)
    ] if is_iterable(iterable) else [iterable]


class cut(list):

    @staticmethod
    def _cut(iterable, *args):
        """Cut a list by index or arg"""
        void = object()
        if not args:
            args = 0,

        if len(args) > 1:
            iterable = cut._cut(iterable, *args[:-1])
        index = args[-1]
        if index == ellipsis:
            return flatten(iterable)

        def cut_item(item):
            if isinstance(item, list) and (
                    isinstance(index, int) or isinstance(index, slice)):
                return (
                    list.__getitem__(item, index)
                    if isinstance(index, slice) or len(item) > index
                    else void)
            if isinstance(item, dict):
                return item.get(index, getattr(item, str(index), void))
            return getattr(item, str(index), void)
        return list(filter(lambda x: x is not void, map(cut_item, iterable)))

    def __getitem__(self, key):
        if not is_iterable(key):
            key = key,
        return self._cut(self, *key)

    def __getattr__(self, key):
        key = key,
        return self._cut(self, *key)


def dmp(thing):
    """Pretty print an object content"""
    pprint({key: getattr(thing, key) for key in dir(thing)})


class ReverseCut(object):

    def __init__(self, key):
        self.key = key

    def __rmod__(self, it):
        return cut(it)[self.key]


class SimpleGetItem(object):

    def __getitem__(self, key):
        return ReverseCut(key)

    def __getattr__(self, key):
        return ReverseCut(key)


_ = SimpleGetItem()

# Use this with import _ as sthg
__builtins__['_'] = SimpleGetItem()
