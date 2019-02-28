# coding: UTF-8

from typing import Set, Any


def get_pair_iter(it):
    it = iter(it)
    var1 = None
    var2 = next(it)
    while True:
        var1 = var2
        var2 = next(it)
        yield (var1, var2)



if __name__ == "__main__":
    for i in get_pair_iter(iter([1,2,3,4,5])):
        print(i)
    
    for i in get_pair_iter(range(5)):
        print(i)