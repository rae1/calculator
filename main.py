import calculator

calc = calculator.Calculator()

print('Hello')
first = input('Enter a number: ')
second = input('Enter another: ')

print('{} plus {} equals {}'.format(first, second, calc.add(first, second))) 
