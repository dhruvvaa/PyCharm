numbers = [1,2,3,4,5,6,7,8,9]
letters = ['a','b','c','d','e','f','g','h','i']

#slicing of tuples
print(numbers[2:5])
even_nums = numbers[1::2]
odd_nums = numbers[::2]
print(even_nums)
print(odd_nums)

#iteration with tuples
for n in numbers:
    print(n ** 2)

#functions with tuples
def area_and_circumference(radius):
    import math
    return (math.pi * radius ** 2, 2 *math.pi * radius)
print(area_and_circumference(5))