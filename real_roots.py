def real_roots (a,b,c):
    '''(int, int, int) -> bool
    Function determines if real roots exist when given values for coefficients of
    a quadratic equation
    '''
    root = b**2 - (4*a*c)
    return(root >=0) #roots must be positive to be real
