def main():
    '''
    This exercise consists in: 
    1) Receiving three integers on input
    2) If they are in crescent order, print "crescent"
    3) Else, print "not in crescent order"
    
    Examples:
    
    Enter a number: 1
    Enter another number: 3
    Enter one more number: 19
    crescent

    Enter a number: 3
    Enter another number: 2
    Enter one more number: 1
    not in crescent order
    
    '''
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = int(input("Digite mais um número: "))

    if a < b < c:
        print("crescent")
    else:
        print("not in crescent order")

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
main()
