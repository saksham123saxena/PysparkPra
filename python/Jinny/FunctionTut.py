import string


def greet() -> string:
    return "Hello World"


def greet1() -> string:
    return 1.1


def sumVariable(a, b):
    c = a + b
    print(f"sum of a & b {c}")


# key - words argument
def greetv1(name, department):
    print(f"name of {name} and department is {department}")


# default argument always follow default argument

def greetv2(name, department, college="NIT KKR"):
    print(f"name is {name} and department is {department} and college is {college}")


# way of using argument in tuple form
def sum_of_element(*num):
    sum = 0
    for ele in num:
        sum += ele
    print(f"sum of all elements {sum}")

# way of using argument with number and variable
def sum_of_element_vat(*num,name):
    sum = 0
    for ele in num:
        sum +=ele
    print(f"sum of number {sum} and name is {name}")

# way of using key-words arguments

def way_of_using_keywords(**kwargs):
    for k,v in kwargs.items():
        print(f"value of key is : {k} and value is : {v}")

'''
*args: mean only passing arguments
**keyargs: mean passing key-value pair arguments
'''

print(greet())
n = greet1()
print(type(n))
sumVariable(12, 21)
greetv1(name="hello", department="CS")
greetv2("hello", "cse")
sum_of_element(1,3,2)
sum_of_element(2,1,3,4)
sum_of_element_vat(1,2,3,name="saksham")
way_of_using_keywords(name1="hello1",name2="hello2",name3="hello3")

