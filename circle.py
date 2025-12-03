import math


def area(r):
    '''
    Returns the area of the circle (The product of squared circle radius and Pi)
	
	Parameters:
		r (float): The radius of the circle
	Return value:
		area (float): The area of the circle
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of the circle (The product of doubled circle radius and Pi)
	
	Parameters:
		r (float): The radius of the circle
	Return value:
		perimeter (float): The perimeter of the circle
    '''
    return 2 * math.pi * r