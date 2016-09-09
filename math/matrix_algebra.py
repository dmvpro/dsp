# Matrix Algebra
import numpy as np
from numpy import matrix


a = matrix([[1,2,3],[2,7,4]])
b = matrix([[1,-1],[0,1]])
c = matrix([[5,-1],[9,1],[6,0]])
d = matrix([[3,-2,-1],[1,2,3]])
u = matrix([6,2,-3,5])
v = matrix([3,5,-1,4])
w = matrix([[1],[8],[0],[5]])

print a.shape #Q1.1
print b.shape #Q1.2
print c.shape #Q1.3
print d.shape #Q1.4
print u.shape #Q1.5
print v.shape
print w.shape #Q1.6

print u+v #Q2.1
print u-v #Q2.2
print 6*u #Q2.3 assuming alpha (scaling multiplier) = 6

#Q2.4
# print np.dot(u, v)   # undefined ?
# ValueError: shapes (1,4) and (1,4) not aligned: 4 (dim 1) != 1 (dim 0)
# NOTE: hand calc = (6*3)+(2*5)+(-3*-1)+(5*4) = 51

print np.linalg.norm(u) #Q2.5 = sqrt(74)

#Q3.1
# print a + c  # undefined as dimensions are incompatible 
# ValueError: operands could not be broadcast together with shapes (2,3)(3,2)

print a - c.transpose() #Q3.2
print c.transpose() + 3*d #Q3.3
print b*a #Q3.4

#Q3.5
# print b*a.transpose()  # undefined as dimensions are incompatible
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

#Q3.6
#print b*c  # undefined as dimensions are incompatible
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

print c*b #Q3.7
print b**4 #Q3.8
print a*a.transpose() #Q3.9
print d.transpose()*d #Q3.10
