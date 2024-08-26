# Simple Calculator for the 4 main opperations with only 2 number inputs

# Functions
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def division(x, y):
	return x / y


print("Enter your two numbers and operations below: \n")

# User input
num1 = float(input("First number: "))
num2 = float(input("Second Number: "))
operation = str(input("Operation: "))

print('')


#Output
if operation == '+':
	print(f'> {add(num1, num2)}')
elif operation == '-':
	print(f'> {subtract(num1, num2)}')
elif operation == '*':
	print(f'> {multiply(num1, num2)}')
elif operation == '/':
	print(f'> {division(num1, num2)}')
else:
	print("Operation not found")