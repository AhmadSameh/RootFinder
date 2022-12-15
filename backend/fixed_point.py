from sympy import *


def fixed_point(expr,numOfIterations,approx):
    roots = []
    x = symbols("x")
    roots += {0}
    iter = 0
    expr = sympify(expr)  #Magic function
    newApprox = float('inf')
    approxList = []
    while(iter < numOfIterations):
        roots += {expr.evalf(subs={x:roots[-1]})}
        newApprox = abs(((roots[-1] - roots[-2]) / roots[-1])) * 100
        approxList += {newApprox}
        if(newApprox < approx):
            break
        iter += 1

    return(roots,approxList)


roots = []
approxList = []

(roots,approxList) = fixed_point("exp(-x)",10,0.1)

print(roots)
print(approxList)