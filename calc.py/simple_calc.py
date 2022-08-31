


from asyncio import open_connection
from pickletools import TAKEN_FROM_ARGUMENT1
from secrets import choice
#from art import logo
#print(logo)



def add(n1,n2):
    return n1 + n2 

def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = float(input("what is your first number?: "))

    for symbols in operations:
        print(symbols)
    operation_continue = True
    while operation_continue :
        choice1= input("pick a symbol from the line above?: ")
        num2 = float(input("what is your next number?: "))
        calc_functions = operations[choice1]
        answer =calc_functions(num1,num2)

        print(f"{num1} {choice1} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer} and 'n' to start a new calculation.: ") =="y":
            num1 = answer

        else:
            operation_continue = False
            calculator()

calculator()



#num3 = int(input("what is your next number?: "))
#choice1= input("pick a symbol from the line above?: ")
#calc_functions = operations[choice1]
#second_answer =calc_functions(calc_functions(num1,num2),num3)

#print(f"{first_answer} {choice1} {num3} = {second_answer}")


