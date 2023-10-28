'''
class attribute : always use with class name
 like that:   Demo.no_of_class+=1
'''

class Demo:
    no_of_class=0
    def __init__(self,name):
        self.name=name
        Demo.no_of_class+=1

    def getting_info(self):
        print("name of class "+self.name+ " no of class : "+str(Demo.no_of_class))

d1=Demo("demo1")
d1.getting_info()

d2=Demo("demo2")
d2.getting_info()
