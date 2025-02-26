"""
illustrates a basic linear data structure in action

author: amyxg
"""

def list_operations():
    # Initialize an empty list
    numbers = []
    
    # Add elements using iteration
    for i in range(1, 6):
        numbers.append(i * 2)  # Adding even numbers: 2,4,6,8,10
    print("Original list:", numbers)
    
    # Search for a value using iteration
    search_value = 6
    found = False
    for i, num in enumerate(numbers):
        if num == search_value:
            print(f"Found {search_value} at position {i}")
            found = True
            break
    if not found:
        print(f"{search_value} not found in list")
        
    # Modify elements using iteration
    for i in range(len(numbers)):
        numbers[i] = numbers[i] + 1  # Add 1 to each number
    print("Modified list:", numbers)
    
    # Calculate sum using iteration
    total = 0
    for num in numbers:
        total += num
    print("Sum of all numbers:", total)

# Run the program
list_operations()