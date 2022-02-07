def main():
    '''
    This exercise consists in:
    1) Receiving on input the values of the coefficients in a
        second-degree polynomial equation (a, b e c, respectively)
    2) Calculate the roots in a quadratic equation 
       ax2 + bx + c = 0
    3) Print, accordingly to the value of Δ, the roots of the expression
    4) If Δ < 0, print "this equation has no existing roots"
       If Δ == 0, print "the double root of this equation is: X"
       If Δ > 0, print "The roots of this equation are X1 and X2
    5) In the case of two existing roots for the equation (Δ > 0),
       they must be printed in crescent order. 
    ''' 
    
    print("Hello, this program calculates the roots in a second-degree polynomial equation (ax²+bx+c = 0), given the coefficients a, b e c")

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    delta = (b ** 2) - (4  * a * c)
    bhaskara1 = ( - b + (delta**(1/2))) / (2 * a)
    bhaskara2 = ( - b - (delta**(1/2))) / (2 * a)

    if delta < 0:
        print("this equation has no existing roots")

    if delta == 0:
        print("the double root of this equation is", bhaskara1)

    if delta > 0:
        if bhaskara1 < bhaskara2:
            print("The roots of this equation are", bhaskara1, "and", bhaskara2)
        else:
            print("The roots of this equation are", bhaskara2, "and", bhaskara1)
          

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

