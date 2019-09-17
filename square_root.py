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
    if positive_number < 0:
        raise ValueError("Input should be a positive number or zero")
    if (positive_number == 0):
        return 0
    else:
        right = positive_number
        result = 0
        left = 0
        return newGuess(left,positive_number,right,positive_number)
def newGuess(left,right,result,positive_number):
    threshold = 0.0000000001
    result = (left+right) / 2.0
    pow2= result*result
    if (abs(pow2 - positive_number) <= threshold):
        return result
    else:
        if (pow2 > positive_number):
            right = result
        else:
            left = result
        return newGuess(left,right,result,positive_number)

