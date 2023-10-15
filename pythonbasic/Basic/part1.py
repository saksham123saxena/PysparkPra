# use for single line comments
'''
it is using for multi-lines,
comments
'''

name="hello"
print(name)

##use of backslash
ans=2+\
    3+\
    4
print("sum of above problem: "+str(ans))


## way of storing string
str1='hello' # for single word
print(str1)

## for statements
str2="this is hello world"
print(str2)

## paragraph
str3="""
this is the hello world,
for giving the multiline solution
"""
print(str3)

## way of taking input
v=input()


print("value of v "+v)

a=2;b=3

## indentation
if a>b :
    print("a is greator than b")
else :
    print("a is lesser than b")


'''
import sys : is very useful for working python code with python shell.

'''

x,y,z = "hello1","hello2","hello3"
print("printing the values of "+x+" - "+y+" - "+z)


'''
global: keyword
'''
val="hello global"

def func():
    val="hello local"
    print(val)

func()
print("variable : "+val)



global val1
val1="hello global"

def func1():
    val1="hello local"
    print(val1)
func1()
print("variable : "+val1)
