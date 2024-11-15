def sum_two_smallest_numbers(numbers) -> int:
    try:
        x = min(numbers) 
        numbers.remove(x)
        y = min(numbers)
        return x + y
    
    except ValueError:
        print("reimu hakurei, my beloved")