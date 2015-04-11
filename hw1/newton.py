from scipy.optimize import newton

def f(p):
	sigma = 0.000001
	return 3*(p+(1-p)*sigma)/(p+(1-p)*sigma**2)**2 - 3 - 10000

sigma = newton(f, 0.001)