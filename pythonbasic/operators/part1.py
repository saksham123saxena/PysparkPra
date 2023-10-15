k=1
# getting the address of the k variable
print(k)
print(id(k))

l=3

'''
is : operator is equivalent == operator
is not : operator is equivalent != operator
in : operator is use for checking element present in list 
not in : operator is use for checking element not present in the list
'''

print(l==k)
print(l!=k)
print(l is k)
print(l is not k)

a=1;b=1
print("address of a and b "+str(id(a))+"   "+str(id(b)))
print("address of k and l "+str(id(k))+"   "+str(id(l)))

li=[1,2,3]
l11=li.copy()
print("address of li and li1 "+str(id(li))+"  "+str(id(l11)))

print("is operator "+str(2 in li))
print("is operator "+str(2 not in li))
