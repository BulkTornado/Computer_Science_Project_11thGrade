#Simple Arithmetic Module

def Welcome():
    print("""
    *************************************************************
    *               SIMPLE ARITHMETIC CALCULATOR                *
    *************************************************************
    
    Welcome! Let's perform some arithmetic calculations.
    
    How to Use the Program:
    1. Enter a number when prompted.
    2. Select the operation you want to perform by entering the number corresponding to your choice.

    --------------------------------------------------------------------------------------
    | IMPORTANT: The program does NOT follow BODMAS OR PEDMAS.                           |
    | Operations are evaluated from left to right.                                       |
    | Example: 2 + 2 * 4 gives 16(incorrect) instead of 10(correct)                      |
    --------------------------------------------------------------------------------------
    """)


Arithmetic_Symbols = {1:'+',2:'-',3:'*',4:'/'}

total, total_output = 0, ''


def PreStart():
    global total, total_output
    while True:
        try:
            total = float(input('\nEnter the first number: '))
            total_output = str(total)
            print(f'Your input till now --> {total_output}')
            break
        except ValueError:
            print('Please enter a valid integer/float')
            continue


def addition(add):
    global total
    total += add

def subtraction(sub):
    global total
    total -= sub

def multiplication(mul):
    global total
    total *= mul

def division(div):
    if div == 0:
        print('Division by 0 is not allowed/defined')
        return
    else:
        global total
        total /= div


def StartModule():
    global total_output
    while True:
        print('\nFrom the following, input a choice:')
        print('1. Addition \t\t\t2. Subtraction '
              '\n3. Multiplication \t\t4. Division '
              '\n0. Exit')
        try:
            user_choice = int(input('Enter your choice (1-4 or 0 to exit): '))
        except ValueError:
            print('Please enter a valid choice!')
            continue
        
        if user_choice == 0:
            print(f'\nThe total is: {total_output} ==> {total:.10f}...')
            print('''

                   ---------------------------------------- 
                   |    Exiting the Arithmetic module.    |
                   ----------------------------------------

                        ''')
            break

        elif user_choice < 1 or user_choice > 4:
            print('\nPlease enter a valid choice!')

        else:
            try:
                user_input = float(input('Enter a number: '))
            except ValueError:
                print('Please enter an integer or float')
                continue
            if user_choice == 1:
                addition(user_input)
            elif user_choice == 2:
                subtraction(user_input)
            elif user_choice == 3 :
                multiplication(user_input)
            elif user_choice == 4:
                division(user_input)

            total_output += ' ' + Arithmetic_Symbols[user_choice] + ' ' + str(user_input)
            print(f'Your current total: {total_output} ==> {total:.10f}')

if __name__ == '__main__':

    Welcome()
    PreStart()
    StartModule()

