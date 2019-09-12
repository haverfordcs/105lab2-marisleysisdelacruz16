def sqrt_iterative(positive_number):
    if positive_number<0:
        raise ValueError("Input should be a positive number or zero")
    else:
        left = 0
        right = positive_number
        result = 0
        threshold = 0.0000000001
        while right - left > threshold:
            result = (left + right) / 2.0
            pow2 = result * result
            if abs(pow2 - positive_number) <= threshold:
                return result
            elif pow2 < positive_number:
                left = result
            else:
                right = result
        return result


# implement the following function
# You must not use built-in libraries like math.sqrt
# Write your own logic

def sqrt_recursive(positive_number):
    if positive_number == 0: # You can comment or remove this block if needed
        return 0
    # <Your code goes here>
