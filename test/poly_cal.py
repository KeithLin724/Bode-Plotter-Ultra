import sympy
import numpy as np

from control.matlab import tf, pole, zero, bode
from matplotlib.pyplot import savefig, show
import os

'''
newPath = os.path.join(os.path.abspath(os.path.curdir), 'tmp')

os.mkdir(newPath)
print(newPath)'''

print(os.path.exists(''))

my_poly = '10'  # "2*x**2+7*x-3"
x = sympy.Symbol('x')
try:
    my_poly = sympy.polys.polytools.poly_from_expr(my_poly)[0]
except Exception as e:

    print(e)
    print('ok')
    # exit()
thing = sympy.Poly(my_poly)

tmp = thing.as_expr()  # my_poly.  # .coeffs()
print(tmp)
print(str(tmp))
print(my_poly)
tmp = sympy.Poly(tmp)

tmp = tmp.all_coeffs()
print(type(tmp), tmp)
'''
tmp = [float(i) for i in tmp]

num, den = np.array(tmp), np.array([1.0])
G = tf(num, den)
pole(G)
zero(G)

print(G)'''
