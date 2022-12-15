from sympy import *


def main():
    # x = symbols("x")
    # y = cos(x)
    # str = "exp(-x) - x"
    # expr = sympify(str)
    # print(expr)
    # z = expr.subs(x,1).evalf()
    # print(z)
    roots = []
    roots += {0}
    roots += {3}
    print(roots[-1],roots[-2])
    # print(y.subs(x,0))

main()