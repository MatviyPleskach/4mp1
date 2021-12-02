import math
x=[1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7] 
y=[10.517,10.193,9.807,9.387,8.977,8.637,8.442,8.482,8.862,9.701,11.132,13.302] 
h = x[1] - x[0]
def smth(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
      return mas
    else:
      j-=1
      return smth(mas, j)
yx1=1/h*smth(y, 1) [1]-smth(y, 2) [1]/2+smth(y, 3) [1]/3-smth(y, 4) [1]/4
yx2=1/h**2*smth(y, 2) [1]-smth(y, 3) [1]+11/12*smth(y, 4) [1]
print (yx1)
print (yx2)
