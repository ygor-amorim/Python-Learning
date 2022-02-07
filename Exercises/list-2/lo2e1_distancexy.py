def main():
   '''
   This exercise consists in:
   1) Receiving 4 numbers on input;
   2) The first two must correspond to the coordinates x and y
      of a dot in a Cartesian plane;
   3) The latter two must correspond to the coordinates x and y
      of ANOTHER dot in the SAME plane;
   4) Calculate the distance between these 2 dots:
      If the distance is >= 10, print: "far"
      Else, print: "close".
      
   The distance between two dots in a Cartesian plane can be
      calculated by the formula:
      d(x,y) = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

       
   '''
   import math
   x1 = int(input("Enter the value of x1: "))
   y1 = int(input("Enter the value of y1: "))
   x2 = int(input("Enter the value of x2: "))
   y2 = int(input("Enter the value of y2: "))


   distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)) 

   if distance >= 10:
       print("far")
   else:
       print("close")
          

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

main()

