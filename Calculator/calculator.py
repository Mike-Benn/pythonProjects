def valuesGrabber():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print('''Arithmetic Operation Values:
            1.  Addition
            2.  Subtraction
            3.  Multiplication
            4.  Division
            5.  Floor Division
            6.  Remainder Division
            7.  Exponential(ex: firstNumber to the power of secondNumber)''')
    operator = int(input('Choose an arithmetic operation: '))
    return a , b , operator

def calculate():
    number1 , number2, choiceValue = valuesGrabber()
    if choiceValue == 1:
        print(number1 + number2)
    elif choiceValue == 2:
        print(number1 - number2)
    elif choiceValue == 3:
        print(number1 * number2)
    elif choiceValue == 4:
        try:
            print(number1 / number2)
        except:
            print('You cannot divide by 0')
    elif choiceValue == 5:
        try:
            print(number1 // number2)
        except:
            print('You cannot divide by 0')
    elif choiceValue == 6:
        try:
            print(number1 % number2)
        except:
            print('You cannot divide by 0')
    elif choiceValue == 7:
        print(number1 ** number2)

calculate()


    