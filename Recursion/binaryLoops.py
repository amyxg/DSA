"""
NOTE: binary recursion - iteratively (using loops)

@amyxg
"""
def binarySearch(x, y):
    """
    Performs binary search on a sorted array to find target value.
    x: sorted array/list
    y: target value to find
    Returns the index of the target if found, otherwise -1
    """
    left, right = 0, len(x) - 1
    while left <= right:
        mid = (left + right) // 2 # mid = middle of index of current search range 
        if x[mid] == y:
            return mid
        elif x[mid] < y:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def runBinarySearch():
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Array: {data}")
    searchValue = int(input("Enter a number from above: "))
    result = binarySearch(data, searchValue) # calling binarySearch function
    if result != -1:
        print(f"Found value {searchValue} at index {result}")
    else:
        print(f"Value {searchValue} not found in array")

if __name__ == "__main__":
    runBinarySearch()