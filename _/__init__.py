# -*- coding: utf-8 -*-
from pprint import pprint

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


def cut(iterable, *args):
    """Cut a list by index or arg"""
    void = object()
    if not args:
        args = 0,

    if len(args) > 1:
        iterable = cut(iterable, *args[:-1])
    index = args[-1]
    if index == ...:
        return flatten(iterable)

    def cut_item(item):
        if isinstance(item, list) and index.isdigit():
            return item[int(index)] if len(item) > int(index) else void
        if isinstance(item, dict):
            return item.get(index, getattr(item, index, void))
        return getattr(item, index, void)
    return list(filter(lambda x: x is not void, map(cut_item, iterable)))


def dmp(thing):
    """Pretty print an object content"""
    pprint({key: getattr(thing, key) for key in dir(thing)})
