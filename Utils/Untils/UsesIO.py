# coding: UTF-8

from typing import List, Set, Type, Any, Iterable

def input_line(type_: Type = str):
    return list(map(type_, input().split()))


def print_2d_list(lst2):
    "¥n".join(["".join(str(v) for v in lst) for lst in lst2])

