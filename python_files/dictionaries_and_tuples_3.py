import math

def circle_calculation(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    diameter = 2*radius
    return area, circumference, diameter

if __name__ == "__main__":
    r = input("Enter a radius:")
    r = float(r)
    area, c, d = circle_calculation(r)
    print(f"area {area}, circumference {c}, diameter {d}")
    
    