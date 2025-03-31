"""
Global Maximum of a Vector/Array/List
- this program will locate the peak within an array/list 

The global maximum is the largest value present in the entire collection of elements. 
It represents the highest point in your data set.

author: amyxg
"""
import time

def warmup():
    """
    determine smallest number in a list

    """
    # given three integers, determine their order
    userInts = input("Enter three intgers separated by spaces: ")
    
    # split each integer to a separate var
    intList = userInts.split()
    a = int(intList[0])
    b = int(intList[1])
    c = int(intList[2])

    # using if-else statements to compare
    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c
    
    print(f"The smallest integer is: {smallest}")

def findGlobalMax(numbers):
    """
    determine biggest number in a list

    numbers: list of ints

    """
    currentMax = numbers[0]

    # loop/iterate through the array, check each number
    for num in numbers: 
        # if int in list is greater than (bigger) current maxiumum
        if num > currentMax:
            # Update if we find a larger value
            currentMax = num

    # return the biggest number
    return currentMax

# timer function to measure actual runtime for diff sizes of inputs:
def measure_performance():
    for size in [1000, 10000, 100000, 1000000, 10000000]:
        # Create array of given size
        test_array = list(range(size))
        
        # Start timer
        start_time = time.time()
        
        # Find max
        max_value = findGlobalMax(test_array)
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

def main():
    listOfNums = [5, 12, 3, 8, 9, 2, 10]
    gMax = findGlobalMax(listOfNums)
    print(f"Global Maximum: {gMax}")
    measure_performance()


if __name__ == "__main__":
    main()
    