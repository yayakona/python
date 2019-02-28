# coding: UTF-8

from typing import List, Set, Type, Any, Iterable

def get_pair_iter(it: Iterable) -> (Any, Any):
    it = iter(it)
    var1 = None
    var2 = next(it)
    while True:
        var1 = var2
        var2 = next(it)
        yield (var1, var2)