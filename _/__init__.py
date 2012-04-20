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


def _cut(iterable, *args):
    """Cut a list by index or arg"""
    void = object()
    if not args:
        args = 0,

    if len(args) > 1:
        iterable = _cut(iterable, *args[:-1])
    index = args[-1]
    if index == ellipsis:
        return flatten(iterable)

    def cut_item(item):
        if isinstance(item, list) and isinstance(index, int):
            return item[index] if len(item) > index else void
        if isinstance(item, dict):
            return item.get(index, getattr(item, str(index), void))
        return getattr(item, str(index), void)
    return list(filter(lambda x: x is not void, map(cut_item, iterable)))


class cut(object):
    def __init__(self, iterable):
        self.iterable = iterable

    def __getitem__(self, key):
        if not is_iterable(key):
            key = key,
        return _cut(self.iterable, *key)


def dmp(thing):
    """Pretty print an object content"""
    pprint({key: getattr(thing, key) for key in dir(thing)})
