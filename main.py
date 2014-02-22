import calculator

calc = calculator.Calculator()

print('Hello')
first = int(input('Enter a number: '))
second = int(input('Enter another: '))
result = calc.add(first, second)
print('{} plus {} equals {}'.format(first, second, result))

print('Ok, let us try something else...')
first = int(input('Enter a number: '))
second = int(input('Enter another: '))
result = calc.multiply(first, second)
print('{} times {} equals {}'.format(first, second, result))


