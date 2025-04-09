"""
CSC249
M2HW1 - Gold Attempt
Amy Santjer
04/09/2025

@amyxg
"""
def binary_search_game():
    """
    A guessing game that uses binary search to find a number chosen by the user.
    The program will try to guess the user's number between 0 and 99 in at most 5 tries.
    
    The user responds with:
    "<" if the guess is too high
    ">" if the guess is too low
    "=" if the guess is correct
    """
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
            return
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
            return
    
    # If we get here, we've used all our guesses
    print(f"I've used all {max_guesses} guesses and couldn't find your number.")
    print(f"Based on your responses, your number must be between {low} and {high}.")

def main():
    """
    Main function to run the binary search guessing game.
    """
    print("Binary Search Guessing Games")
    print("-" * 30)
    binary_search_game()
    
    # Ask if the user wants to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again == 'y':
            print("\n" + "-" * 30)
            binary_search_game()
        elif play_again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()