# Menu Driven Scientific Calculator

# User will be asked what would they like to do
# Based on that, the corresponding custom module's functions will be called


count_module = 0
try:
    import SimpleArithmeticModule as SAM
except ModuleNotFoundError:
    count_module += 1
    pass
try:
    import UnitConversionModule as UCM
except ModuleNotFoundError:
    count_module += 1
    pass
try:
    import TrigFuncModule as TFM
except ModuleNotFoundError:
    count_module += 1
    pass


def display_menu():
    print('-' * 78)
    print('| Choose an option from one of the following:                                |')
    print('| 1. Simple Arithmetic\t\t\t2. Unit Conversion                           |'
          '\n| 3. Trigonometry\t\t\t\t0. Exit (Stop the scientific calculator!)    |')
    print('-' * 78)


def StartScientificCalculator():
    print(f'{'':=^180}')
    print(f'{'|                               |':=^180}')
    print(f'{'|     SCIENTIFIC CALCULATOR     |':=^180}')
    print(f'{'|                               |':=^180}')
    print(f'{'':=^180}\n')

    while True:

        display_menu()

        try:
            user_choice = int(input('\nEnter your choice: '))
        except ValueError :
            print('Please enter a valid choice!')
            continue

        if user_choice == 0 :
            print()
            print(f'{'':=^180}')
            print(f'{'|                               |':=^180}')
            print(f'{'|     SCIENTIFIC CALCULATOR     |':=^180}')
            print(f'{'|        EXITING PROGRAM        |':=^180}')
            print(f'{'|                               |':=^180}')
            print(f'{'':=^180}')
            break

        elif user_choice != 0 and 1 <= user_choice <= 3:

            if user_choice == 1 :
                try:
                    SAM.Welcome()
                    SAM.PreStart()
                    SAM.StartModule()
                except NameError:
                    print('\nIt seems the SimpleArithmeticModule has not been installed.'
                          '\nPlease do so before using this section of the Scientific Calculator again.'
                          '\nRemember to restart the Scientific Calculator once you have installed the required module!\n')

            elif user_choice == 2 :
                try:
                    UCM.StartModule()
                except NameError:
                    print('\nIt seems the UnitConversionModule has not been installed.\n'
                          'Please do so before using this section of the Scientific Calculator again.\n'
                          'Remember to restart the Scientific Calculator once you have installed the required module!\n')

            elif user_choice == 3 :
                try:
                    TFM.StartModule()
                except NameError:
                    print('\nIt seems the TrigFuncModule has not been installed.\n'
                          'Please do so before using this section of the Scientific Calculator again.\n'
                          'Remember to restart the Scientific Calculator once you have installed the required module!\n')

        else:
            print('\nPlease enter a valid choice from the given options\n')


if __name__ == "__main__":
    if count_module == 3:
        print("\nIt seems none of the required modules are installed.")
        print("Please install SimpleArithmeticModule, UnitConversionModule, and TrigFuncModule.")
        print("Exiting the Scientific Calculator...")
    else:
        if count_module > 0:
            print(
f'''
   ----------------------------------------------------------------------------------------------
   | Warning: {count_module} module(s) are missing.                                                          |
   | You can still use the Scientific Calculator, but some functionalities may not be available.|
   ---------------------------------------------------------------------------------------------- 
''')

        StartScientificCalculator()

