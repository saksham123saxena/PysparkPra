"""
return statement with function :
function in python can return the one more values.
if you return the more than one values in functions then it will convert into the tuple
"""
import statistics
import math


def sum_a_b(a, b):
    return a + b


def return_multiple_val(name, roll):
    name_title = name.title()
    return name_title, roll


# calculating the mean | median and mode
def mean_median_mode(list):
    return statistics.mean(list), statistics.median(list), statistics.mode(list)


print(f"sum of 2 and 6 is : {sum_a_b(2, 6)}")
return_val = return_multiple_val("hello", 23)
print(type(return_val))
print(return_val)
a, b, c = mean_median_mode([1,2,3,4,5,74,8])
print(f"mean is {round(a,2)} and median is {b} and mode is {c}")
