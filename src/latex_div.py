'''
This is a library  for bode_drawer_GUI
Written by Keith Lin (KYLiN)
Date : 2022/2/28
'''

import matplotlib.pyplot as plt
from sympy import Poly
from sympy.abc import x
from numpy.polynomial.polynomial import Polynomial


def to_math_equ(math_coff: list[int]) -> str:
    math_p = Polynomial(math_coff[::-1])
    math_sp = Poly(reversed(math_p.coef), x)
    return str(math_sp.as_expr()).replace('**', '^')


def div_str_latex(a: str, b: str) -> str:
    return '\\frac{' + a + '}' + '{'+b+'}'


def latex_div(lat: str, path: str) -> None:
    plt.clf()
    # add text
    plt.text(0.3, 0.6, r"$%s$" % lat, fontsize=20)
    # hide axes
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    plt.savefig(path)
    plt.clf()
    plt.close()


def to_latex_div_png(upperPolyList: list[int], lowerPolyList: list[int], path: str) -> None:
    upperPolyStr, lowerPolyStr = to_math_equ(
        math_coff=upperPolyList), to_math_equ(math_coff=lowerPolyList)

    outLatex = div_str_latex(a=upperPolyStr,
                             b=lowerPolyStr).replace('x', 's').replace('1.0*', '')
    latex_div(lat=outLatex, path=path)
