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
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        i=0
        first_number = 0
        second_number = 1
        sum = second_number
        for i in range(n-2):
            sum = first_number + second_number
            first_number = second_number
            second_number= sum
    return sum




