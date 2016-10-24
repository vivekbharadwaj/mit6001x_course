from math import tan,pi
def polysum(n,s):
    '''
    PURPOSE
    *******
    This function should sum the area and square of the perimeter 
    of the regular polygon
    
    ARGUMENTS
    *********
    n: number of sides of polygon 
    s: Each side has length s
    
    RETURNS
    *******
    The function returns the sum, rounded to 4 decimal places.
    
    TO DO
    *****
    no error checking has been done. 
    '''
    area = 0.25*n*s*s/tan(pi/n)
    perimeter = n*s
    
    return round(area+perimeter**2,4)