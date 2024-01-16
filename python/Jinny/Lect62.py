import math


def paint_calculation(height, width, coverage):
    area = height * width
    paint_req = math.ceil(area / coverage)
    print(f"paint requirement is {paint_req}")


h = int(input("Please enter the height of wool:\n"))
w = int(input("Please enter the weight of wool:\n"))
coverage = 7

paint_calculation(h, w, coverage)

