# -*- coding: utf-8 -*-
from pprint import pprint


def cut(iterable, index=0):
    """Cut a list by index or arg"""
    void = object()

    def cut_item(item):
        if isinstance(item, list) and isinstance(index, int):
            return item[index] if len(item) > index else void
        if isinstance(item, dict):
            return item.get(index, getattr(item, str(index), void))
        return getattr(item, str(index), void)
    return list(filter(lambda x: x is not void, map(cut_item, iterable)))


def dmp(thing):
    """Pretty print an object content"""
    pprint({key: getattr(thing, key) for key in dir(thing)})
