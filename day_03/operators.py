# Day 3: 30 Days of python programming
# Exercises

age:int
height:float
complex_number:complex

# calculate the area of a triangle
base_of_triangle = int(input('Enter base: '))
height_of_triangle = int(input('Enter height: '))
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
print('The area of the triangle is',int(area_of_triangle))

# calculate the perimeter of a triangle
A = int(input('Enter side a: '))
B = int(input('Enter side b: '))
C = int(input('Enter side c: '))
perimeter_of_triangle = A + B + C
print('The perimeter of the triangle is',int(perimeter_of_triangle))

# calculate the perimeter and area of a rectangle
length_of_rect = int(input('Enter the length: '))
width_of_rect = int(input('Enter the width: '))
area_of_rect = length_of_rect * width_of_rect
perimeter_of_rect = 2 * (length_of_rect + width_of_rect)
print('The are of the rectangle is', area_of_rect)
print('The perimeter of the rectangle is', perimeter_of_rect)

# calculate the area and circumference of a circle
radius_of_circle = int(input('Enter the radius: '))
PI = 3.14
area_of_circle = PI * radius_of_circle * radius_of_circle
circum_of_circle = 2 * PI * radius_of_circle
print('The are of the circle is', area_of_circle)
print('The circumference of the circle is', circum_of_circle)

# calculate slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2
slope = m
x_intercept = b
y_intercept = -b / m
print('The slope is', slope)
print('The x-intercept is', x_intercept)
print('The y-intercept is', y_intercept)

# calculate the slope and euclidean distance of (2,2) and (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10

slope_of_points = (y2 - y1)/(x2 - x1)
euclidean_distance = ((x2 - x1)* (x2 - x1) + (y2 - y1)*(y2 - y1))**0.5
print('Slope:', slope_of_points)
print('Euclidean distance', euclidean_distance)

# comparing slopes
print(slope == slope_of_points)

# calculate the equation y = x^2 + 6x + 9
a = 1
b = 6
c = 9

x_1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
x_2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
print('The solution for the quadratic equation is',x_1,x_2)

# length of a string
len_of_python = len('python')
len_of_dragon = len('dragon')
print('The length of dragon is', len_of_dragon)
print('The length of python is', len_of_python)
print(len_of_python > len_of_dragon)

# on in dragon and python
print('on' in 'python' and 'on' in 'dragon')

# in operator
print('jargon' in 'I hope this course is not full of jargon')

# negation of on in dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# float to string
len_of_python_float = float(len_of_python)
len_of_python_string = str(len_of_python_float)
print(len_of_python_string)

# check if number is even or not
number = int(input('Enter the number: '))
if number % 2 == 0 :
   print(True)
else:
    print(False)

# floor division
print(7 // 3 == int(2.7))

# type check
print('10' == 10)

# calculate pay of a person
hours_worked = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earning = hours_worked * rate_per_hour
print(weekly_earning)

# how long can you live
years_lived = int(input('Enter number of years you have lived: '))
seconds_lived = 60 * 60 * 24 * 365 * years_lived
print(f'You have lived for {seconds_lived} seconds.')

# display table
print('1', 1, 1*1, 1*1*1)
print('2', 1, 2*2, 2*2*2)
print('3', 1, 3*3, 3*3*3)
print('4', 1, 4*4, 4*4*4)
print('5', 1, 5*5, 5*5*5)