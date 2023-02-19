import math

#1Write a Python program to convert degree to radian.
deg = int(input())
rad = float(deg / 180)
rad1 = rad * 3.14285
print('%.6f' % rad1)

#2.Write a Python program to calculate the area of a trapezoid.
h = input("Height:")
a = input("Base, first value:")
b = input("Base, second value:")
print("S =",((a + b)/2)*h)

#3
n = int(input("Number of sides:"))
s = int(input("Length of the side:"))
area = (n * s * s) / (4 * math.tan(math.pi/n))
print(area)



#4Write a Python program to calculate the area of a parallelogram.
l = int(input("Length of base:"))
H = int(input("Height of parallelogram:"))
print(l * H)
