def add(numbers: str) -> int:
    if numbers:
        if ',' in numbers:
            x = numbers.split(',')
            return int(x[0]) + int(x[1])
        return int(numbers)

    return 0
