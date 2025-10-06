def get_valid_series():
    """
    Get a valid series of positive numbers from user input.
    Returns a list of positive numbers (at least 3).
    """
    while True:
        try:
            user_input = input("Enter at least 3 positive numbers (space-separated): ")
            
            # Split the input and convert to float
            numbers = []
            for num_str in user_input.split():
                num = float(num_str)
                if num <= 0:
                    print("Error: All numbers must be positive (> 0). Please try again.")
                    break
                numbers.append(num)
            else:
                # Check if we have at least 3 numbers
                if len(numbers) < 3:
                    print("Error: You must enter at least 3 numbers. Please try again.")
                    continue
                
                return numbers
                
        except ValueError:
            print("Error: Invalid input. Please enter only numbers separated by spaces.")


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("Series Analyzer - Menu")
    print("1. Input a new series")
    print("2. Display the series (original order)")
    print("3. Display the series (reversed order)")
    print("4. Display the series (sorted low→high)")
    print("5. Display the Max value")
    print("6. Display the Min value")
    print("7. Display the Average value")
    print("8. Display the Number of elements")
    print("9. Display the Sum of the series")
    print("0. Exit")
    print("="*60)


def display_result_header(title):
    """Display a formatted header for results."""
    print("\n" + "="*60)
    print(title)
    print("="*60)


def format_series(numbers):
    """Format the series for display, showing integers without decimal points."""
    formatted = []
    for num in numbers:
        if num == int(num):
            formatted.append(str(int(num)))
        else:
            formatted.append(str(num))
    return " ".join(formatted)


def handle_option_1():
    """Handle option 1: Input a new series."""
    return get_valid_series()


def handle_option_2(series):
    """Handle option 2: Display the series in original order."""
    display_result_header("Series (Original Order)")
    print(format_series(series))


def handle_option_3(series):
    """Handle option 3: Display the series in reversed order."""
    display_result_header("Series (Reversed Order)")
    reversed_series = series[::-1]
    print(format_series(reversed_series))


def handle_option_4(series):
    """Handle option 4: Display the series sorted from low to high."""
    display_result_header("Series (Sorted Low→High)")
    sorted_series = sorted(series)
    print(format_series(sorted_series))


def handle_option_5(series):
    """Handle option 5: Display the maximum value."""
    display_result_header("Max value")
    max_val = max(series)
    if max_val == int(max_val):
        print(int(max_val))
    else:
        print(max_val)


def handle_option_6(series):
    """Handle option 6: Display the minimum value."""
    display_result_header("Min value")
    min_val = min(series)
    if min_val == int(min_val):
        print(int(min_val))
    else:
        print(min_val)


def handle_option_7(series):
    """Handle option 7: Display the average value."""
    display_result_header("Average value")
    average = sum(series) / len(series)
    print(f"{average:.2f}")


def handle_option_8(series):
    """Handle option 8: Display the number of elements."""
    display_result_header("Number of elements")
    print(len(series))


def handle_option_9(series):
    """Handle option 9: Display the sum of the series."""
    display_result_header("Sum of the series")
    total = sum(series)
    if total == int(total):
        print(int(total))
    else:
        print(total)


def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("\nChoose an option [0-9]: ")
            choice_num = int(choice)
            if 0 <= choice_num <= 9:
                return choice_num
            else:
                print("Error: Please enter a number between 0 and 9.")
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """Main program function."""
    print("Welcome to Series Analyzer!")
    print("=" * 40)
    
    # Get initial series
    series = get_valid_series()
    
    # Main program loop
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print("\nThank you for using Series Analyzer!")
            break
        elif choice == 1:
            series = handle_option_1()
        elif choice == 2:
            handle_option_2(series)
        elif choice == 3:
            handle_option_3(series)
        elif choice == 4:
            handle_option_4(series)
        elif choice == 5:
            handle_option_5(series)
        elif choice == 6:
            handle_option_6(series)
        elif choice == 7:
            handle_option_7(series)
        elif choice == 8:
            handle_option_8(series)
        elif choice == 9:
            handle_option_9(series)


if __name__ == "__main__":
    main()
