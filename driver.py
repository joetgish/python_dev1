# 3 May 2015
# Joe Welch
# Python 2.7
# Program used to develop baseline for workshop to introduce
# Python, GitHub, collective work
#
# Dev notes:
# 
# 5/3/2015 
# Began library dev effort to compare runtimes and 
# accuracies of various numerical integration techniques
# Trapezoidal rule
 # Used numpy library (EnThought version)
 # Key statement is 
 #  s = y[0] + 2 * sum(y[1:n]) + y[n]
 # numpy sum function sums y values in one statement - elegant


# ______________________________________________________
import numpy as np

def f(x):
	# defines the function to be used for numerical integration
	return 2.0 * (x**2) - x - 4.0


def trapezoid(f, a, b, n, debug = False):
	 x = np.linspace(a, b, n+1)
	 y = f(x)

	 if debug:
	 	for i in range(n-1):
	 		print "%5d %10.4f %10.4f" % (i, x[i], y[i])

	 s = y[0] + 2 * sum(y[1:n]) + y[n]
	 h = float(b - a) / n
	 return s * h / 2.0

def main():
	a = 0.0
	b = 5.0
	n = 10
	s = trapezoid(f, a, b, n, True)
	print s



if __name__ == '__main__':
	main()
