from sympy import *
def bisection(expr,l,u,max_iterations,epislon):
    z=expr.subs(x,l)*expr.subs(x,u)
    if z > 0 :
        return 0
    if expr.subs(x,l) < 0:
        l_sign=0
    else :
        l_sign=1

    Approximations_roots=[max_iterations]
    Precision=[max_iterations]
    mid=(l+u)/2
    i=0
    while(i < max_iterations):
        mid_temp=mid
        mid=(l+u)/2
        if(expr.subs(x,mid)< 0)  :
            if(l_sign == 0) :
                l=mid
            else :
                u=mid
        else :
            if(l_sign == 1):
                l=mid
            else:
                u=mid
        Approximations_roots.insert(i,mid)
        if(i == 0):
            Precision[0]=0
        else :
            Precision.insert(i,abs((mid-mid_temp)/mid))
        
        print(i,Approximations_roots[i],Precision[i])
        if(Precision[i] < epislon and i != 0):
            return
        i=i+1
    return Approximations_roots,Precision


if __name__ == "__main__":
    x=symbols('x')
    expr=(pow(x,4) - 2 * pow(x,3) -4* pow(x,2)+4*x+4) 
    bisection(expr,-2,-1,20,.01) 

        



    

