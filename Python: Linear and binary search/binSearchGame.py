"""
CSC249
M2HW1 - Gold Attempt
Amy Santjer
04/09/2025

@amyxg
"""
def binarySearch(numbers, key):
    """
    Performs a binary search on a sorted list to find a specific key.
    Prints each step of the process to visualize how the algorithm works.
    
    Args:
        numbers (list): A sorted list of integers
        key (int): The value to search for
        
    Returns:
        int: The index of the key if found, -1 otherwise
    
    Time Complexity: O(log n), where n is the length of the list
    """
    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts with entire range.
    low = 0
    high = len(numbers) - 1
    
   
    print("Starting binary search for", key, "in list:", numbers)
    print("-" * 60)
    
    # Loop until "low" passes "high"
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2
        
        # Print the current search state
        print(f"  Search range: indexes {low} to {high}")
        print(f"  Middle index: {mid}, Middle value: {numbers[mid]}")
        
        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1
            print(f"  {numbers[mid]} < {key}, thus will search right half..")
      
        elif (numbers[mid] > key):
            high = mid - 1
            print(f"  {numbers[mid]} > {key}, thus will search left half..")
      
        else:
            print(f"  {numbers[mid]} = {key}, key found at index {mid}!")
            return mid   
        
        step += 1
        print("-" * 60)
   
    print(f"Key {key} not found in the list")
    return -1 # not found


def binarySearchDemo():
    """
    Demonstration of the binary search algorithm.
    Takes user input as a comma-separated list of numbers, sorts it,
    and performs a binary search for a specified key.
    """
    print("\nBINARY SEARCH DEMONSTRATION")
    print("─" * 30)
    print("This demo shows how binary search works step by step.\n")
    
    # Get input from user as a comma-separated string
    input_str = input("Enter numbers, separated by commas: ")
    
    # Convert the input string to a list of integers
    numbers = [int(num.strip()) for num in input_str.split(',')]
    
    # Sort the list in ascending order
    original = numbers.copy()
    numbers.sort()
    
    if original != numbers:
        print('Original numbers:', original)
    print('Sorted numbers:', numbers)
        
    key = int(input('Enter an integer value to search for: '))
    print()  # Add a blank line for readability
    
    key_index = binarySearch(numbers, key)
    print()  # Add a blank line for readability
        
    if (key_index == -1):
        print(f'Result: {key} was not found.')
    else:
        print(f'Result: Found {key} at index {key_index}.')
    
    input("\nPress Enter to return to the main menu...")


def binarySearchGame():
    """
    A guessing game that uses binary search to find a number chosen by the user.
    The program will try to guess the user's number between 0 and 99 in at most 5 tries.
    
    The user responds with:
    "<" if the guess is too high
    ">" if the guess is too low
    "=" if the guess is correct
    """
    print("\nBINARY SEARCH GUESSING GAME")
    print("─" * 30)
    print("Think of a number between 0 and 99 (WHOLE NUMBER).")
    print("I'll try to guess it in 5 or fewer attempts.")
    print('Respond with "<" if my guess is too high,')
    print('             ">" if my guess is too low,')
    print('             "=" if my guess is correct.\n')
    
    # Variables to hold the low and high boundaries of search space
    low = 0
    high = 99
    
    # Track the number of guesses
    guesses = 0
    max_guesses = 5
    
    # Loop until we find the number or run out of guesses
    while guesses < max_guesses:
        # Calculate the middle of the current range
        mid = (high + low) // 2
        
        # Increment guess counter and make a guess
        guesses += 1
        print(f"Guess #{guesses}: Is your number {mid}?")
        
        # Get user's response
        response = input("Your response (<, >, or =): ").strip()
        
        # Process the response
        if response == "=":
            print(f"Great! I found your number {mid} in {guesses} guesses!")
            break
        elif response == "<":
            # Number is lower, adjust high boundary
            high = mid - 1
            print(f"Searching between {low} and {high}")
        elif response == ">":
            # Number is higher, adjust low boundary
            low = mid + 1
            print(f"Searching between {low} and {high}")
        else:
            # Invalid response, don't count this guess
            print("Please enter either '<', '>', or '='")
            guesses -= 1
        
        # Check if search space is invalid (user might be giving inconsistent responses)
        if low > high:
            print("Hmm, something's not right. Your responses are inconsistent.")
            break
    
    # If we get here and didn't find the number, we've used all our guesses
    if guesses == max_guesses and response != "=":
        print(f"I've used all {max_guesses} guesses and couldn't find your number.")
        print(f"Based on your responses, your number must be between {low} and {high}.")
    
    input("\nPress Enter to return to the main menu...")


def displayMenu():
    """
    Displays the main menu options.
    
    Returns:
        int: The user's choice (1, 2, or 3)
    """
    print("\n" + "─" * 50)
    print("BINARY SEARCH PROGRAMS".center(50))
    print("─" * 50)
    print("1. Binary Search Demo")
    print("2. Binary Guess the Number Game")
    print("3. Quit")
    print("-" * 50)
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main function that displays a menu and runs the selected program.
    """
    while True:
        choice = displayMenu()
        
        if choice == 1:
            binarySearchDemo()
        elif choice == 2:
            binarySearchGame()
        elif choice == 3:
            print("\nProgram ending....Goodbye!....")
            break


if __name__ == "__main__":
    main()