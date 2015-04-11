import numpy as np
from numpy.linalg import inv

R = np.matrix( ((1,0,2), (0,1,-1)) )
r = np.matrix( ((4), (0.5)) ).transpose()
s2 = 1.5
b = np.matrix( (1,2,1) ).transpose()
XX = np.matrix( ((2,1,0), (1,2,1), (0,1,2)) )
m = 2

F = (R*b-r).transpose() * inv(R*XX*R.transpose()) * (R*b-r) / m / s2
print np.rank(R)