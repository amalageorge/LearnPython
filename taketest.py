num1 = input("Enter the first number")

num2 = input("Enter the second number")

print "Enter the opertor"
operator = raw_input()

result = 0

if operator == '+':
	result = num1 * num2

elif operator == '-':
	result = num1 - num2

elif operator == '*':
	result = num1 * num2


elif operator == '/':
	result = num1 / num2

elif operator == '%':
	result = num1 % num2

print result
