'''
reduce function : is not present in python,
for using reduce, you have use module of func Tools for working with reduce function
'''

from functools import reduce as r

# print(help(r))

'''
reduce(...)
    reduce(function, iterable[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.

None

'''

def sumt(a,b):
    return a+b

num=[1,2,3,4,4]

print(r(sumt,num))
print(r(lambda x,y:x+y,num))
