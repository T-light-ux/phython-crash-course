#Area of a circle
"""
Calculate the area of a circle
"""
pi = 3.142
radius = 7
area_of_circle = pi * (radius**2)
# print(area_of_circle)
print(f"The area of the circle is: ", {area_of_circle})


'''
This program is written to calculate the simple
interest of money
'''
principal = p = int(input("Please enter the value of principal:  "))
rate = r = int(input("Please enter the rate: "))
time = t = int(input("Please enter the time period here: "))

simple_interest = (p * r * t) / 100
print(simple_interest)
print(type(simple_interest))

