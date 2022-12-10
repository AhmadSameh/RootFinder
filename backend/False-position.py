from sympy import *
def False_position(expr,l,u,max_iterations,epislon):
    z=expr.subs(x,l)*expr.subs(x,u)
    if z > 0 :
        return 0
    if expr.subs(x,l) < 0:
        l_sign=0
    else :
        l_sign=1

    Approximations_roots=[max_iterations]
    Precision=[max_iterations]
    x_new=(((expr.subs(x,u)*l)-(expr.subs(x,l)*u))/(expr.subs(x,u)-expr.subs(x,l)))
    i=0
    while(i < max_iterations):
        x_temp=x_new
        x_new=(((expr.subs(x,u)*l)-(expr.subs(x,l)*u))/(expr.subs(x,u)-expr.subs(x,l)))
        if(expr.subs(x,x_new)< 0)  :
            if(l_sign == 0) :
                l=x_new
            else :
                u=x_new
        else :
            if(l_sign == 1):
                l=x_new
            else:
                u=x_new
        Approximations_roots.insert(i,x_new)
        if(i == 0):
            Precision[0]=0
        else :
            Precision.insert(i,abs((x_new-x_temp)/x_new))
        
        print(i,"{0:.8f}".format(Approximations_roots[i]),"{0:.8f}".format(Precision[i]))
        if(Precision[i] < epislon and i != 0):
            return
        i=i+1
    return Approximations_roots,Precision


if __name__ == "__main__":
    x=symbols('x')
    expr=(pow(x,4) - 2 * pow(x,3) -4* pow(x,2)+4*x+4) 
    False_position(expr,-2,-1,11,.01) 

        



    

