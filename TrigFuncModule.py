# Trigonometric Functions Module

import math

Trig_Functions = {1:'sin',2:'cos',3:'tan'}

def Trigonometry(angle, trigonometry_choice, user_input_angle, user_choice_angle, trigon_choice):

    trigonometry = {'sin':math.sin(angle),'cos':math.cos(angle),'tan':math.tan(angle)}

    print(f'\nThe {trigonometry_choice} of {user_input_angle}{user_choice_angle} = {trigonometry[trigon_choice]:.3f}')

def StartModule():
    global Trig_Functions
    print("""
        *************************************************************
        *                 TRIGONOMETRY CALCULATOR                   *
        *************************************************************

        Welcome! Let's calculate the value of trigonometric functions.

        How to Use the Program:
        1. Enter a number when prompted.
        2. Choose the trig func of your choice.
        3. Enter the unit of angle and the angle itself.

        --------------------------------------------------------------------------------------
        | IMPORTANT: The tan of 90.0° is undefined, and not equal to 16331239353195370.000   |
        --------------------------------------------------------------------------------------
        """)

    while True:
        print('\nFrom the following, input a choice:')
        print('1. sin\t\t2. cos\t\t3. tan')

        try:
            trig_choice = int(input('Enter your choice\t: '))
            trig_choice = Trig_Functions[trig_choice]
        except KeyError:
            print(f'\n--> Invalid choice! Please enter a number from 1-3 <--')
            continue
        except ValueError:
            print(f'\n--> Invalid input! Please enter a number from 1-3 <--')
            continue

        print('\nFrom the following, input a choice:')
        print('1. Degree\t2. Radian')

        try:
            angle_choice = int(input('Enter your choice\t: '))
        except ValueError:
            print(f'\n--> Invalid input! Please enter 1 for degree and 2 for radian <--')
            continue
        if angle_choice not in (1,2):
            print(f'\n--> Invalid choice! <--')
            continue
        else:
            try:
                angle_input = float(input('\nEnter the angle\t: '))
            except ValueError:
                print(f'\n--> Invalid angle input! <--')
                continue

            if angle_choice == 1:
                angle_radian, angle_choice = math.radians(angle_input), '°'
                Trigonometry(angle_radian, trig_choice, angle_input, angle_choice, trig_choice)

            elif angle_choice == 2:
                angle_radian, angle_choice = angle_input, ' rad'
                Trigonometry(angle_radian, trig_choice, angle_input, angle_choice, trig_choice)

        cont = input('\nDo you want to perform another calculation? (y/n) ')

        if cont.lower().strip() not in 'yes':
            print('''

                   --------------------------------------------- 
                   |     Exiting the Trigonometric module.     |
                   --------------------------------------------- 

                        ''')
            break

if __name__ == '__main__':
    StartModule()

