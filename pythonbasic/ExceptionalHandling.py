'''
try: use for initialize the file handling concept
except: use for printing the error
else: if any error is not coming then you can print the error block msg
finally: block is use for printing the either msg is coming or not
raise: for raising the exception or exception argument
sys.exit(1): also use for raising the exception [NOTE: before using it import sys]

NOTE imp: alternative of exception handling, we can use Logger 
'''

# sal=1
# try:
#     print(sal)
# except NameError:
#     print("name error")
# else :
#     print("error is not coming")
# finally:
#     print("final block")


'''
EXCEPTIONAL argument
'''
# try:
#     print(sal)
# except Exception as argu:
#     print("except block : "+str(argu))
# finally:
#     print("===============Exceptional Error===============")

sal=-1
try:
    if sal<0:
        raise Exception("Salary can't be negative")
except Exception as ar:
    print("Exceptional Block: "+str(ar))
