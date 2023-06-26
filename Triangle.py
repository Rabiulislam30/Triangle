#Python program to find the area of Triangle
a = 7
b = 8
c = 9

#Uncomment below to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))


#calculate the semI-perimeter
s = (a + b + c)/2

#calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area)
