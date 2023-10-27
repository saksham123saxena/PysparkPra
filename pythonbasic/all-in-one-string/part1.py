text="this is string"
print(text)
print("type of text "+str(type(text)))
arr=[1,2,3]
print(arr)
print("type of arr "+str(type(arr)))

## we can iterate over the python string
# for x in text :
#     print(x)

##
print(text[0:3])
print(text[-1])

## for reversing the string in python
print(text[::-1])

'''
there are some important operators are associated with string 
- * : using for multiplication string
- + : using for concatenate the string
- in : using for checking the substring in the provided string
- not in : using for checking the substring is not present in the provided string
- %s : using for refer the string 
- %d : using for refer the integer 
- \n : using for new line
- \ : using for adding space 
- dir(str) : using for show all function, which are present in the string class 
- help(str.find) : using for documentation of the string function
'''

## - *
s="this is the python string"
print(s)
print("after the * : "+s*3)

print("hello %s program, i wrote more than %d times "% ('WORD',100))

y="""
this is 
HELLO WORD
program in 
python
"""
y1="this is\n HELLO WORD program in\n python"
print(y1)

y2="this is \"python\" "
print(y2)

print(dir(str))

print(y2.center(50))
print(y2.zfill(50))

print("count of i in the given string "+str(y2.count('i')))  ## getting the number of count i
print(y2.find('i')) ## getting the location of i
y4='    hello    '
print(y4.strip())  ## removing the empty space of provided string

print(y.startswith('t'))  # checking provided string is start with t or not

# using the join function in the string
y5="spark"
print("#**".join(y5))

# using of split
y6="this is python"
print(y6.split(' ')) # split function : return type is an array

# using way of  split line
y7="this is the python \n and it is easy to use"
print(y7.splitlines())

# using the replace function in string
y8=" this is the python"
print(y8.replace('python','PYTHON'))
