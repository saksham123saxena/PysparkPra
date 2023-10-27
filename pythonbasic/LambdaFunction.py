'''
lambda function :
-there is no restriction in argument it can have, but it can have only one expression
-lambda function can not be direct call any print function, because lambda function requires an expression
'''

demo=lambda x:x+10
adding=lambda a,b:a+b
def generic(num):
    return lambda x:x*num

print(demo(10))

print(adding(1,2))
print(generic((10)))  # imp: way of creating generic function
double=generic(2)
triple=generic(3)
print(double(10))
print(triple(10))
