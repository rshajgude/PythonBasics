
# Positional argument and keyword argument
# Default argument value

# area function with 1 argument
def area_circle(radius):
    area=3.24*(radius**2)
    return area

# area of rectangle with 2 parameters , with default parameters
def area_rectangle(height, length=5):
    area=length*height
    return area

# area of cylinder
def area_cylinder(radius, height=15):
    area=2*3.14*(radius**2) + 2*3.14*radius*height
    return area


print(f"Area of circle with radius 5 is {area_circle(5)}")
print(f"Area of rectangle with height 5 and length 10 is {area_rectangle(5, 10)}")
print(f"Area of rectangle with height 5 is {area_rectangle(5)}") # default 5 is used

print(f"Area of cylinder with height 5 and radius 10 is {area_cylinder(10, 5)} correct ")
print(f"Area of cylinder with height 5 and radius 10 is {area_cylinder(5, 10)} wrong")
print(f"Area of cylinder with height 5 and radius 10 is {area_cylinder(height=5, radius=10)} correct")

print(f"Area of cylinder with radius 5 is {area_cylinder(5)} default height=15 is used") # default height=15 is used
