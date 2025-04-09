"""
NOTE: Linear search sequentially checks each element in a list, 
starting from index 0 and proceeding until either finding the target value or reaching the end. 

While simple to implement and requiring no sorting, it has O(n) time complexity, 
making it less efficient than binary search for large datasets. 
The implementation below demonstrates this straightforward approach.

@amyxg
"""

def linear_search(numbers, numbers_size, key):
    for i in range(numbers_size):
        if numbers[i] == key:
            return i
    return -1  # not found

def main():
    numbers = [2, 4, 7, 10, 11, 32, 45, 87]
    NUMBERS_SIZE = 8
    
    print("NUMBERS: ", end="")
    for i in range(NUMBERS_SIZE):
        print(numbers[i], end=" ")
    print()
    
    key = int(input("Enter a value: "))
    
    key_index = linear_search(numbers, NUMBERS_SIZE, key)
    
    if key_index == -1:
        print(f"{key} was not found.")
    else:
        print(f"Found {key} at index {key_index}.")

if __name__ == "__main__":
    main()