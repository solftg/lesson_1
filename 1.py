from math import *

a = int(input("Введите значение аргумента"))

z1 = (sin(radians(pi/2 + 3*a))) / (1 - sin(radians(3 * a - pi)))
z2 = 1 / (tan(radians(5*pi/4 + 3*a/2)))


print(ceil(z1 * 1000)/1000, ceil(z2 * 1000)/1000)