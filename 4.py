import numpy as np
#1 (2)
A = np.matrix ([[2,3,1],[-1,1,0],[1,2,-1]])

B = np.matrix ([[1,2,1],[0,1,2],[3,1,1]])
print("AB-BA =", A*B - B*A)

#2
C = np.matrix([[-1,2],[0,1]])
print("Mult C =", np.linalg.matrix_power(C,2))

#3 (2)
B1 = np.matrix ([[5,8,-4],[6,9,-5],[4,7,-3]])
B2 = np.matrix ([[3,2,5],[4,-1,3],[9,6,5]])

print ("A1*A2 =", B1 * B2)

#4 (2)
A1 = np.matrix('0,2,0;3,4,5;6,7,8')
det_A1 = np.linalg.det(A1)
det_A1 = round(np.linalg.det(A1),2)
print ("determinant A1 =", A1)

#5 (2)
BB1 = np.matrix('2,3,4,1;1,2,3,4;3,4,1,2;4,1,2,3')
det_A1 = np.linalg.det(A1)
det_A1 = round(np.linalg.det(A1),2)
print ("determinant BB1 =", BB1)

#6 (2)
AA = np.matrix([[2,5,7],[6,3,4],[5,-2,-3]])
AA = np.linalg.inv(AA)
print("Inverse matrix AA =", AA)

#7 
aa = np.matrix([[1,2,3,4],[3,-1,2,5],[1,2,3,4],[1,3,4,5]])
rank = np.linalg.matrix_rank(aa)
print ("Matrix rank = ", rank)
