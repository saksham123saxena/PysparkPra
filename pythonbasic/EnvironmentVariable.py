import os
print(dir(os.environ))
'''
['_MutableMapping__marker', '__abstractmethods__', '__class__', '__class_getitem__', '__contains__', 
'__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', 
'__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', 
'__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_data', 'clear', 'copy', 
'decodekey', 'decodevalue', 'encodekey', 'encodevalue', 'get', 'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values']

'''

print(os.environ['JAVA_HOME'])
