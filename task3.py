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
print(round (simple_interest))
print(type(simple_interest))

#Calculation for valu of 100 / 25
num1 = 100
num2 = 25
divide_two_num = num1 / num2
print(round (divide_two_num))
print(type(divide_two_num))


'''
Program that returns a user's
full name
'''
first_name = str (input ("Your first name"))
middle_name = str (input ("Your middle name"))
last_name = str (input ("Your last name"))
full_name = last_name + middle_name + first_name
print (f"Here is your full name: {full_name}")


'''
Solution to average age of 
six boys in school
'''
age_of_first_boy = 19
age_of_second_boy = 16
age_of_third_boy = 26
age_of_forth_boy = 17
age_of_fifth_boy = 22
age_of_sixth_boy = 18

total_age_of_six_boys = (age_of_first_boy + age_of_second_boy + age_of_third_boy + age_of_forth_boy + age_of_fifth_boy + age_of_sixth_boy)
average_age_of_six_boys = (total_age_of_six_boys) / 6
print (f"average of the boys: round {average_age_of_six_boys}")


'''
Conversion from celsius
to fahrenheit 
'''
C = float(input("Enter the temperature of Celsius in °C: "))
F = (1.8 * C) + 32
print(f"Temperature in Fahrenheit is {F}")


