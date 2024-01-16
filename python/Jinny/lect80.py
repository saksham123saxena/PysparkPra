"""
what is the local scope and global score in python

"""
a = 10
b = 10


def display():
    a = 110
    print("local scope ", a)


def display_v1():
    global b
    b = 110
    print("local scope ", a)


print("global scope ", a)
display()
print("global scope ", a)

print("use of the global score")
print("global scope ", b)
display_v1()
print("global scope ", b)


