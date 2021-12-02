from scipy import integrate
from numpy import *
from math import log
def f(x):
    return 1/sqrt(3 * x + 1)
s,err = integrate.quad(f, 1.4, 2.2)
print(f'Rectangle method = {s}')

def f3(x):
    return 1 / sqrt(x**2 + 0.8)

def tr(f3, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f3(a) + f3(b))
    for i in range(1, n + 1):
        sum += f3(a + i + h)
    return sum * h

print(f"Trapezoid = {tr(f3, 1.6, 0.6, 20)}")
s, err = integrate.quad(f3, 1.6, 0.6)
print(f'Trazepoid check = {s}')

def f2(x):
    return (log10(x**2 + 2))/ (x + 1)
def trf2(f2, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f2(a) + f3(b))
    for i in range(1, n + 1):
        sum += f2(a + i + h)
    return sum * h
print(f'Simpson = {trf2(f2, 1.4, 2.2, 8)}')
s, err = integrate.quad(f2, 1.4, 2.2)
print(f'Simpson check = {s}')
