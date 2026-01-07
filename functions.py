def hello10():
    print("Hello "*10)

def pyramid(layers):
    star = '*'
    for i in range(0,layers):
        print(star.center(layers*2, ' '))
        star += '**'

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def surface_area_cuboid(l,w,h):
    """This function takes in length, width, and height of a cuboid and returns surface area of cuboid."""
    return 2*(l*w+w*h+h*l)

hello10()
pyramid(10)
print(circle_area(10))
print(surface_area_cuboid(10,10,10))
print(surface_area_cuboid.__doc__)