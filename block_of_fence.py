"""
'Docstring'
Here is a phython code  that calculates the amount
of blocks needed to fence a piece of land
regardless of the size
"""
length_of_land = int (input ("please enter the length of the land in feet: feet"))
width_of_land = int (input ("please enter the width of the land in feet: feet"))
perimeter_of_land = 2 * (length_of_land + width_of_land)

#Using f-string print formatting
print(f"Here is the perimeter of the land in feet: {perimeter_of_land} feet")

#converting feet to metre
length_in_metre = round (perimeter_of_land * 0.3048) 
print(f"Here is the length in metre: {length_in_metre}")

#Space for gate
space_for_gate = int(input("please entre the space for gate in feet"))
space_for_gate_metre = round (space_for_gate * 0.3048)
print(f"the space for gate in metre is: {space_for_gate_metre} metre") 

# Total length of land needed for fencing
total_length_of_land = length_in_metre - space_for_gate_metre
print(f"The total length of land for fencing is: { total_length_of_land} metre")


"""
Block dimension:
6 inches: 450mm x 150mm
9 inches: 450mm x 225mm
"""
length_of_block = int(input("please enter the length of the block: mm "))
length_of_block_metre = length_of_block / 1000
num_of_courses = int(input("please entre the number of courses: "))

first_course = round (total_length_of_land / length_of_block_metre)
print(f"The number of blocks for the first course are: {first_course} blocks")
total_blocks = num_of_courses * first_course
print(f"The number of blocks needed for {num_of_courses} courses are: {total_blocks}")

