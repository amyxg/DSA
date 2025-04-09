"""
NOTE: 

@amyxg
"""
def binary_search(numbers, key):
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
    
    step = 1  # To track the step number in the search process
   
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
            print(f"  {numbers[mid]} < {key}, so search right half")
      
        elif (numbers[mid] > key):
            high = mid - 1
            print(f"  {numbers[mid]} > {key}, so search left half")
      
        else:
            print(f"  {numbers[mid]} = {key}, key found at index {mid}")
            return mid   
        
        step += 1
        print("-" * 60)
   
    print(f"Key {key} not found in the list")
    return -1 # not found


def main():
    """
    Main function to demonstrate the binary search algorithm.
    Takes user input as a comma-separated list of numbers, sorts it,
    and performs a binary search for a specified key.
    """
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
    
    key_index = binary_search(numbers, key)
    print()  # Add a blank line for readability
        
    if (key_index == -1):
        print(f'Result: {key} was not found.')
    else:
        print(f'Result: Found {key} at index {key_index}.')

if __name__ == "__main__":
    main()