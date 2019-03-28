def roots (a,b,c):
    '''(float, float, float) -> none
    Function calculates the roots of a quadratic function with provided coefficients
    '''

    #Calculate positive root
    posRoot = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
    #Calculate negative root
    negRoot = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)
    print('The quadratic equation with coefficients a =' + ' ' + str(a) + ' ' + ',b =' + ' ' + str(b) + ' ' + ',and c =' + ' ' + str(c) + ' ' +
          'has the following solutions (ie roots)' + ' ' + str(posRoot) + ' ' + 'and' + ' '+ str(negRoot) + ' ' + '.')
