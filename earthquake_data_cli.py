import json

from earthquake_data import EarthquakeData


def ask_for_input(prompt):
    """
    a function to ask for input and check it based off of if its a number or not
    :return: a valid input
    """
    valid = False
    while not valid:
        valid_input = input(prompt)
        try:
            valid_input = int(valid_input)
            valid = True
        except ValueError:
            print("Invalid input.")

    return valid_input

def print_choices(choices):
    for choice in choices:
        print(f"{choice}: {choices[choice]}")


def earthquake_data_cli():
    """
    Function to allow the user to interact with earthquake_data.py
    """
    print("Hello! Please choose from the following:")
    input_choices = {
        1:"Past hour data",
        2:"Past day data",
        3:"Past week data",
        4:"Past month data",
        5:"Quit"
    }
    print_choices(input_choices)
    input_choice = ask_for_input("> ")

    all_earthquake_data = EarthquakeData()

    while input_choice != 5:
        if input_choice == 1:
            past_hour_data = all_earthquake_data.past_hour_data()
            print(json.dumps(past_hour_data["features"],indent=2))
            print_choices(input_choices)
            input_choice = ask_for_input("> ")
        elif input_choice == 2:
            past_day_data = all_earthquake_data.past_day_data()
            print(json.dumps(past_day_data["features"],indent=2))
            print_choices(input_choices)
            input_choice = ask_for_input("> ")
        elif input_choice == 3:
            past_week_data = all_earthquake_data.past_week_data()
            print(json.dumps(past_week_data["features"],indent=2))
            print_choices(input_choices)
            input_choice = ask_for_input("> ")
        elif input_choice == 4:
            past_month_data = all_earthquake_data.past_month_data()
            print(json.dumps(past_month_data['features'],indent=2))
            print_choices(input_choices)
            input_choice = ask_for_input("> ")
        else:
            print("Invalid input")
    print("Ending interaction...")

def main():
    earthquake_data_cli()

if __name__ == "__main__":
    main()


