import math
def func(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return area, circum

a, c = func(5)
print(f"{a:.2f}, {c:.2f}")