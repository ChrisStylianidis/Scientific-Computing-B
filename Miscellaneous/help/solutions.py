#bisection method
def func(x):
    return (tipos tis f)

while (b-a) > eps:
    c = (a+b)/2.0
    fc = func(c)
    if fc == 0:
        a=0
        b=0         
    if fc * fa > 0:     
        a = c           
        fa = fc
    else:
        b = c          
        fc = fc

#NEWTON RAPHSON
#
def f(x):
    return (eksisosi)
#
def df(x):
    return (paragogos)
#
def newton(x0,eps,istepmx):
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2 ##an to flag einai 2 to vrikame
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error   
        x0 = x1           
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1 ##An to flag einai ena den vrethike i lisi
            break
#
    return x0,flag,istep#x0 einai i lisi mou,istep ta vimatapou ekane
#otan valeis to proto x0 na einai mia timi opoia dipote extos apo f'(x0)=0
