def sum_num(numbers):
    
    total = 0
    for x in numbers:
        total += x
    
    # THE BUG: Used integer division (//) instead of float division (/)
    # This truncates the decimal part, returning an integer.
    # Example: 10 / 4 = 2.5, but 10 // 4 = 2
    if len(numbers) == 0:
        return 0
    return total // len(numbers)