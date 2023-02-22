from math import sqrt

a = int(input())
b = int(input())
c = int(input())

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x2, x1)
elif d == 0:
    x = -b / (2 * a)
    print(x)

