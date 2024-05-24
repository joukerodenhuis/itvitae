print("")
print("What function would you like to call? This program has x() and Calculator(). Type out x() or C() for either function respectively.")
FunctionToCall = input()
print("")

def Calculator(N1, Operator, N2):
    N1 == int(N1)
    Operator == str(Operator)
    N2 == int(N2)
    if Operator == "/" and N2 == 0:
        print("You can't divide by zero!")
        print("")
        exit()
    match Operator:
        case "+":
            return N1 + N2
        case "-":
            return N1 - N2
        case "*":
            return N1 * N2
        case "/":
            return N1 / N2
        case _:
            print("The valid operators are + - * / , try again")
            print("")
            exit()

def x():
    print("Hello world")
    print("")
    
match FunctionToCall:
    case "x()":
        x()
        exit()
    case "C()":
        I1 = int(input("Please provide the first integer: "))
        print("")
        ProvidedOperator = input("Please provide the operator. It must be one of the following: * / - +: ")
        print("")
        I2 = int(input("Please provide the second integer: "))
        print("")
        Answer = Calculator(I1, ProvidedOperator, I2)
        print(Answer)
        print("")
        exit()
    case _:
        print("This program only has x() and C(). Please try again.")
        print("")
        exit()

