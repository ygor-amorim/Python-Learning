'''
This exercise consisted in creating an empty rectangle 
accordingly to the numbers submitted on input
'''
l = int(input("enter the lenght: "))
h = int(input("enter the height: "))
lenght = l
height = h
while h >= 1:
    while l > 1:
        if (h == height or h == 1 or l == lenght or l == 1):
            print("#", end = "")
        else:
            print(" ", end = "")
        l = l - 1
    print("#")
    h = h - 1
    l = lenght
