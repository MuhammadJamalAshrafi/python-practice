# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
#    Equation of an area of a triangle is,
#    area = (1/2)*base*height
def calculate_triangle_area(base, height):
    return (1 / 2) * base * height

print(f"Area of a trianlge is : {calculate_triangle_area(10, 5)}")

# 2. Modify above function to take third parameter shape type.
#    It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
#    rectangle area=length*width
def calculate_area(dimension_one, dimension_two, shape):
    if shape == "triangle":
        area = (1 / 2) * dimension_one * dimension_two
    elif shape == "rectangle":
        area = dimension_one * dimension_two
    else:
        print("Error: Input shape is neither trianlge nor rectangle.")
        area = None    
    return area

print(f"Area of shape is : {calculate_area(10, 5, "rectangle")}")

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
def print_pattern(n):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s += '*'
        print(s)
print_pattern(3)
