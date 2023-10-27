def func(*arr):
    print("value of argument arrray "+str(arr[2]))

def func1(**stu):
    print("value of student id "+str(stu["id"]))

print("function calling")
func("hello","word","program","in","python","language")
func1(name="hello",id=13)

