"""
NOTE: Linear search is a search algorithm that starts from the beginning of a list, 
and checks each element until the search key is found or the end of the list is reached. 
The linear_search() function shown below compares each item in a given list, one at a time.

@amyxg
"""

def linear_search(names, key):
    for i in range(len(names)):
        # If the key value is found, the index is returned     
       if (names[i] == key):
           return i

    # If the key value is not found, -1 is returned.
    return -1  # not found

# Main program to test the linear_search() method   
names = ["amy", "xiong", "santjer", "scarlett", "johns", "sebash", "jane", "doe"]
print('Names:', names)
     
key = input('Enter an string value: ')
key_index = linear_search(names, key)

if (key_index == -1):
    print('%s was not found.' % key)
else:
    print('Found %s at index %d.' % (key, key_index))