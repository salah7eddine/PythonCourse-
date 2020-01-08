# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function


""" def sayHello(name):
    print(f'Hello {name}')

sayHello('Abousaid Hamza') """


def sayHello(name='Mizo'):
    print(f'Hello {name}')


sayHello()

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total


sum = getSum(3, 4)
print(sum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def getSum(num1, num2): return num1 + num2


print(getSum(10, 4))
