import os
'''
way of reading file
'''
# f=open("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orders.txt")
# print(type(f))
# print("print the file pointer location "+str(f.tell()))
# print(f.read())  ## it will print the content of file
# print("print the file pointer location "+str(f.tell()))
# f.seek(15) ## reset the location of file pointer
# print("print the file pointer location "+str(f.tell()))
# print(f.read())  ## it will print the content of file
# f.close() # using for closing the file
# print(f.readline()) ## use to print the line of the content file

'''
way of writing the file:
we have two way of writing in file
1: override
2: append

-- have three way of creating the file
1. x : file must not be already available
2. a : file the content in existing file
3. w : file the content the file
-- rename and removing the file name : we have to import os
-- and also using the existing file
'''
f = open("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/temp1.tx", "a")
f.write("it is checked by me")
f.close()

# f = open("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/temp.tx", "a")
# f.write("Now the file has more conzzztent!")
# f.close()

#open and read the file after the appending:
# f = open("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/temp1.tx", "r")
# print(f.read())

## renaming the file
if os.path.exists("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/temp1.tx"):
    print("FILE EXISTS")
else:
    print("FILE IS NOT EXISTS")
