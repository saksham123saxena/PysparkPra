'''
__name__ : is one of the special variable
basically it is representing the current file module.
one point -: in python, every file has one super module, which is __main__
'''

import SubClassSpecialVariable as sub

sub.sub()
def main():
    print("inside the main function")
    print(__name__)

if __name__ == '__main__':
    main()


'''
output of above example:

it is Sub class, for understanding the concept of __name__ special variable #printing part of sub function
SubClassSpecialVariable #name of class, because here __name__ is targeting the sub class
inside the main function #printing the main function printing statement
__main__ # here __name__, because this class is targeting the main class

'''
