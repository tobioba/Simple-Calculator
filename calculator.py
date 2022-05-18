num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
op = input('Enter the Oprator: ')

if op == '+':
    print('The addtion is ', num1+num2)
elif op == '-':
    print('The subtraction is ', num1-num2)
elif op == '*':
    print('The multiplication is ', num1*num2)
elif op == '/':
    print('The Division is ', num1/num2)
else:
    print('invalid Operator')