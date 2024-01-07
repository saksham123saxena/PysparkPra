# print(help(map))

'''
class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

'''

frameworks=["spark","iceberg","flink"]
li=map(str.upper,frameworks)
print(list(map(str.upper,frameworks)))


id
handle
encrypted_phone
str_arr=["a","b","c","d","e","f"]
num_arr=[1,2,3,4,5]
print(list(map(lambda x,y : (x,y), str_arr,num_arr)))
