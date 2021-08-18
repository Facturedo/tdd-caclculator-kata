def add(numbers: str) -> int:
    if numbers:
        if ',' in numbers:
            int_numbers = [int(x) for x in numbers.split(",")]

            sum_value = 0
            for value in int_numbers:
                sum_value = sum_value + value
            
            return sum_value
        
        return int(numbers)

    return 0
