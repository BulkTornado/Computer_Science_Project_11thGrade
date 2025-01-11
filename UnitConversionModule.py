#Unit Conversion Module

def convert_length(value, from_unit, to_unit):
    # Define conversion factors for length
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.344,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    }

    # Convert the value to meters first
    value_in_meters = value * length_units[from_unit]

    # Convert the value in meters to the target unit
    converted_value = value_in_meters / length_units[to_unit]

    return converted_value

def convert_mass(value, from_unit, to_unit):
    # Define conversion factors for mass
    mass_units = {
        'grams':1,
        'kilograms':1000,
        'milligrams':0.001,
        'micrograms':0.000001,
        'tonne':1000000,
        'ounce':28.35,
        'pound':453.6,
        'US ton':9071581

    }

    # Convert the value to kilograms first
    value_in_kilograms = value * mass_units[from_unit]

    # Convert the value in kilograms to the target unit
    converted_value = value_in_kilograms / mass_units[to_unit]

    return converted_value

def convert_time(value, from_unit, to_unit):
    # Define conversion factors for time
    time_units = {
        'seconds':1,
        'milliseconds':0.001,
        'microseconds':0.000001,
        'minute':60,
        'hour':3600,
        'day':86400,
        'week':604800,
        'month':2.628E6,
        'year':31536000
    }

    # Convert the value to seconds first
    value_in_seconds = value * time_units[from_unit]

    # Convert the value in seconds to the target unit
    converted_value = value_in_seconds / time_units[to_unit]

    return converted_value

def display_menu():
    print("\nUnit Conversion Menu:")
    print("1. Length")
    print("2. Mass")
    print("3. Time")
    print("0. Exit\n")

def StartModule():
    print("""
        *************************************************************
        *                 UNIT CONVERSION CALCULATOR                *
        *************************************************************

        Welcome! Let's do some unit conversions!

        How to Use the Program:
        1. Enter a number wherever prompted.
        2. Choose the physical quantity that you would like to convert.
        3. Enter the unit of your value, then the unit you want to convert to convert to.
        4. At last, enter the value itself.

        --------------------------------------------------------------------------------------
        | IMPORTANT: You can only convert between different units of length, mass, and time. |
        --------------------------------------------------------------------------------------
        """)

    # Display menu
    while True:
        display_menu()
        try:
            choice = int(input("Choose the type of conversion (1-3 or 0 to exit): "))
        except ValueError:
            print('\nPlease enter a valid choice!')
            continue

        if choice == 0:
            print('''
            
       ----------------------------------------------- 
       |     Exiting the Unit Conversion module.     |
       -----------------------------------------------
            
            ''')
            break

        # Choose units for length
        elif choice == 1:
            print("\nLength Units:")
            length_units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
            for index, unit in enumerate(length_units, 1):
                print(f"{index}. {unit}")

            try:
                from_choice = int(input("\nChoose the unit to convert from (1-8): ")) - 1
                to_choice = int(input("Choose the unit to convert to (1-8): ")) - 1
            except ValueError:
                print('Invalid input! Please choose from any of the options')
                continue

            if from_choice != to_choice:
                try:
                    value = float(input(f"Enter the value in {length_units[from_choice]}: "))
                    converted_value = convert_length(value, length_units[from_choice], length_units[to_choice])
                    print(
                    f'''\n{value} {length_units[from_choice]} ==> {converted_value:.10f} {length_units[to_choice]}''')
                except ValueError:
                    print('Please enter a valid number to convert!')
                    continue
            else:
                print("You chose the same units. No conversion necessary.")

        elif choice == 2:
            print('\nMass Units:')
            mass_units = ['grams','kilograms','milligrams','micrograms','tonne','ounce','pound','US ton']
            for index, unit in enumerate(mass_units, 1):
                print(f"{index}. {unit}")

            try:
                from_choice = int(input("\nChoose the unit to convert from (1-8): ")) - 1
                to_choice = int(input("Choose the unit to convert to (1-8): ")) - 1
            except ValueError:
                print('Invalid input! Please choose from any of the options')
                continue

            if from_choice != to_choice:
                try:
                    value = float(input(f'Enter the value in {mass_units[from_choice]}: '))
                    converted_value = convert_mass(value, mass_units[from_choice], mass_units[to_choice])
                    print(f"{value} {mass_units[from_choice]} is equal to {converted_value:.10f} {mass_units[to_choice]}")
                except ValueError:
                    print('Please enter a valid number to convert!')
                    continue
            else:
                print("You chose the same units. No conversion necessary.")

        elif choice == 3:
            print('\nTime Units:')
            time_units = ['seconds','milliseconds','microseconds','minute','hour','day','week','month','year']
            for index, unit in enumerate(time_units, 1):
                print(f'{index}. {unit}')

            try:
                from_choice = int(input('\nChoose the unit to convert from (1-9): ')) - 1
                to_choice = int(input('Choose the unit to convert to (1-9): ')) - 1
            except ValueError:
                print('Invalid input! Please choose from any of the options')
                continue

            if from_choice != to_choice:
                try:
                    value = float(input(f'Enter the value in {time_units[from_choice]}: '))
                    converted_value = convert_time(value, time_units[from_choice], time_units[to_choice])
                    print(f'{value} {time_units[from_choice]} is equal to {converted_value:.10f} {time_units[to_choice]}')
                except ValueError:
                    print('Please enter a valid number to convert!')
                    continue
            else:
                print('You chose the same units. No conversion necessary.')
        # You can add more conversions for mass and time similarly
        else:
            print("\nInvalid choice. Please choose a valid conversion type from 1-3 or 0 to exit!")


# Start the conversion program
if __name__ == '__main__':
    StartModule()
