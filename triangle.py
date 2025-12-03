def area(a, h):
	'''
	Returns the area of the triangle (The product of triangle side and triangle height division by 2)

	Parameters:
		a (float): The triangle side
		h (float): The triangle height
	Return value:
		area (float): The area of the triangle
	'''
	return a * h / 2

def perimeter(a, b, c):
	'''
	Returns the perimeter of the triangle (The sum of triangle sides)

	Parameters:
		a (float): The first triangle side
		b (float): The second triangle side
		c (float): The third triangle side
	Return value:
		perimeter (float): The perimeter of the triangle
	'''
	return a + b + c