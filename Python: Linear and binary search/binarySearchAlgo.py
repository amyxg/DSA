"""
NOTE: Binary search is performed on a sorted list. It compares the middle element of the list to the key

@amyxg
"""

def binary_search(numbers, key):
    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts with entire range.
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid   
   
    return -1 # not found


# Main program to test the binary_search() function   
numbers = [2.22, 4.4, 7.711, 10.015, 11.1, 32.329, 45.45, 87.7]
print('NUMBERS:', numbers)
     
key = float(input('Enter an integer value: '))
key_index = binary_search(numbers, key)
     
if (key_index == -1):
    print('%.3f was not found.' % key) # %.3f shows 3 decimal places
else:
    print('Found %.3f at index %d.' % (key, key_index))