from numpy import array
from numpy import matrix
from numpy.linalg import inv


a_1 = array((1,1,1,1,1))
a_X = array((1,2,3,4,5))
a_Y = array((1,4,9,16,25))

X = matrix([(a_1),(a_Y)]).transpose()
Y = matrix([a_X]).transpose()

beta = inv(X.transpose()*X) * X.transpose() * Y
print beta

'''
epsilon = Y - X*beta
n = 10
p = 3 - 1
s2 = epsilon.transpose() * epsilon / (n-p)
print s2

print float(s2) * inv(X.transpose()*X)


X = [1,2,3,4,5]
Y = [1,4,9,16,25]
a = 6
b = -7

s = 0
for i in range(5):
	s += (Y[i]-a*X[i]-b)*(2*X[i]+3)
print s
'''