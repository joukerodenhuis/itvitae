#A calculator! I will have so many + operators, the performance will be amazing!

ValidOperators = ['*', '/', '+', '-']

print("What operator do you want to use? Choose:")
print(" + - / * ")
OperatorChoice = str(input())
print(" ")

if OperatorChoice not in ValidOperators:
	print("The input you provided is not valid. Try again")

# Asking for a number and checking if its actually a number.	
ValidNumberInput = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("What will be the first number? This calculator only works with integers")
FirstNumber = int(input())
print(" ")

print("What will be the second number?")
SecondNumber = int(input())
print(" ")

if OperatorChoice == "/" and SecondNumber == 0:
	print("You can't divide by zero! Try again")
	exit()

match OperatorChoice:
	case "+":
		result = FirstNumber + SecondNumber
		print(f"Your answer is: {result}")
	case "-":
		result = FirstNumber - SecondNumber
		print(f"Your answer is: {result}")
	case "/":
		result = FirstNumber / SecondNumber
		print(f"Your answer is: {result}")
	case "*":
		result = FirstNumber * SecondNumber
		print(f"Your answer is: {result}")