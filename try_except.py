# Just getting some practice with try-except blocks

def get_valid_input():
    # Try to capture valid user input
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input <= 0:
            # When this error is raised, it triggers the except block
            raise ValueError("Input must be a positive integer.")
        # When the if condition preceding raise is false, this part of the
        # function simply returns the user_input
        return user_input
    # Except block handles the exception raised by raise, a ValueError,
    # and assigns the exception type to the variable 'e'
    except ValueError as e:
        print(f"Error: {e}")
        return get_valid_input()  # Retry recursively until valid input is provided

valid_input = get_valid_input()
print(f"You entered: {valid_input}")