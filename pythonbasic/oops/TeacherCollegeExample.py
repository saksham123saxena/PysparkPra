import os
class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def get_salary(self):
        return "salary of "+self.name+" is "+str(self.salary)
    def get_name(self):
        return self.name

# class for college
class College:
    def __init__(self,col_name):
        self.col_name=col_name
        self.Teacher=[]

    def getting_col_info(self):
        print("name of college "+str(self.col_name))
        print("college teacher info !")
        for ele in self.Teacher:
            print(ele.get_name())

    def adding_teacher_name(self,t):
        self.Teacher.append(t)


t1=Teacher("Robert",31,90000)
print(t1.get_salary())


t2=Teacher("Chrish",30,90000)
print(t2.get_salary())

c1=College("Oxbery")
c1.adding_teacher_name(t1)
c1.adding_teacher_name(t2)
c1.getting_col_info()
