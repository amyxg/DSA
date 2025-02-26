"""
NOTE: fibonacci series recursion -  recursively (using functions that call themselves repeatedly)

@amyxg
"""
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    n: The position in the Fibonacci sequence (0-indexed)
    Returns: The nth Fibonacci number
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n-1) + fibonacci(n-2)


def callFibonacci():
    # Display the first 10 Fibonacci numbers
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    
    # Demonstrate calculating a specific Fibonacci number
    n = int(input("\nEnter an integer to calculate a specific Fibonacci number: "))
    result = fibonacci(n)
    print(f"fibonacci({n}) = {result}")
    
    # Show the sequence up to this number
    print(f"\nFibonacci sequence up to {n}:")
    sequence = [fibonacci(i) for i in range(n+1)]
    print(sequence)

if __name__ == "__main__":
    callFibonacci()