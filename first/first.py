print("hello world")
# 鸡你太美
print("你好，我叫方清")
'''
多行注释
'''


# Step 1 & 2: Define a recursive function to calculate factorial
def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive step
        return n * factorial(n - 1)

# Example usage of the factorial function
print(f"Factorial of 5 is: {factorial(5)}")
print(f"Factorial of 0 is: {factorial(0)}")
print(f"Factorial of 1 is: {factorial(1)}")