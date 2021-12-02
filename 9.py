import numpy as np
from math import factorial

x=[0.180, 0.185, 0.190, 0.195, 0.200, 0.205,0.210]
y=[5.5154, 5.4669, 5.3263, 5.1930, 5.0664, 4.9461,4.8317]
x1=0.184
x2=0.209

h = x[1] - x[0]
q1 = (x1 - x[0]) / h
q2 = (x2 - x[-1]) / h

def n(y,j):
  mas = []
  for i in range(len(y)):
    mas.append(y[i] - y[i-1])
  mas.pop(0)
  if j == 1:
    return mas
  else:
    j -= 1
    return n(mas, j)
    
s1_1 = y[0] + q1 * n(y,1)[0] + q1 * (q1-1) * n(y,2)[0] / factorial (2)
s2_1 = q1 * (q1-1) * (q1-2) * n(y,3)[0] / factorial (3)
s3_1 = q1 * (q1-1) * (q1-2) * (q1-3) * n(y,4)[0] / factorial (4)
s4_1 = q1 * (q1-1) * (q1-2) * (q1-3) * (q1-4) * n(y,5)[0] / factorial (5)

d1 = s1_1 + s2_1 + s3_1 + s4_1
print("1st Newtons interpolation -", d1)

s1_2 = y[5] + q2 * n(y,1)[4] + q2 * (q2+1) * n(y,2)[3] / factorial (2)
s2_2 = q2 * (q2+1) * (q2+2) * n(y,3)[2] / factorial (3)
s3_2 = q2 * (q2+1) * (q2+2) * (q2+3) * n(y,4)[1] / factorial (4)
s4_2 = q2 * (q2+1) * (q2+2) * (q2+3) *(q2+4) * n(y,5)[0] / factorial (5)

d2= s1_2 + s2_2 + s3_2 + s4_2
print("2nd Newtons interpolation-", d2)
