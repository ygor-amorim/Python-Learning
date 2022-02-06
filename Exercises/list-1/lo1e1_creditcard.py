# This exercise consists in printing the credit card bill from
# a fictitious person based on user

def main():
    name = input("Enter the client name: ")
    day = input("Enter the due date: ")
    month = input("Enter the due month: ")
    value = input("Enter the value of the bill: ")

    print("Hello,",name)
    print("Your bill due to", day, "from month", month, "in the total amount of $%s is now closed."%(value))

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . .

main()
