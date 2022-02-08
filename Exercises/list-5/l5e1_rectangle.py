'''
This exercise consisted in creating a rectangle accordingly to 
the numbers submitted on input
'''
lenght = int(input("enter the lenght: "))
height = int(input("enter the height: "))
l = lenght
h = height

while height >= 1:
    while lenght > 1:
        print("#", end="")
        lenght = lenght - 1
    print("#")
    lenght = l
    height = height - 1
    
    