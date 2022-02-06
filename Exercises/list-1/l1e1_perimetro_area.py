# This simple exercise consists in calculating and printing 
# the perimeter and area of a square based on the value of one
# of the sides.

side = int(input("Please, enter the value corresponding to one of the sides of your square: "))

x = 4 * side
y = side ** 2

print("perimeter: %i area: %i"%(x, y))