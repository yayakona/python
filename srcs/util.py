
from typing import List, Set, Type, Any, Iterable

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"*********************************            input          *************************************************"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_input_line(type_: Type):
    return list(map(type_, input().split()))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"*********************************           string          *************************************************"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_splits_list(org_str: str, seqs: List[str]) -> List[str]:
    edit_str = org_str
    for i, seq in enumerate(seqs[:-1]):
        edit_str = edit_str.replace(seq, seqs[i+1])
    return edit_str.split(seqs[-1])

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"*********************************         iterator          *************************************************"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_pair_iter(it: Iterable) -> (Any, Any):
    it = iter(it)
    var1 = None
    var2 = next(it)
    while True:
        var1 = var2
        var2 = next(it)
        yield (var1, var2)

def get_yyy_format_title(title: str, N: int=75) -> str:
    edit_str  = ""
    edit_str += "*" * 60

    edit_str += "*" * 60

def fizz_buzz(stop=100):
    for i range(1,stop):
        print((("Fizz" if not i%3)+("Buzz") if not i%5) or i)

"""
input=3
======
*
**
***
======

input=5
======
*
**
***
****
*****
======
"""
def print_ast(cnt):
    for i in range(cnt):
        print("*"*i)

if __name__ == "__main__":
    for i in get_pair_iter(iter([1,2,3,4,5])):
        print(i)