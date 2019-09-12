def nth_fibonacci_using_recursion(n):
    if n < 0:
        raise ValueError("n should be a positive number or zero")
    else:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return nth_fibonacci_using_recursion(n - 2) + nth_fibonacci_using_recursion(n - 1)


# Implement the following function using iteration i.e. loop
# You can use any loop constructs
def nth_fibonacci_using_iteration(n):
    # You can completely remove the following code if needed
    if n < 0:
        raise ValueError("n should be a positive number or zero")
    if n == 1:
        return 0
