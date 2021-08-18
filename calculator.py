def add(numbers: str) -> int:
    if numbers:
        if ',' in numbers:
            x = numbers.split(',')
            tmp = 0
            for i in x:
                tmp = tmp + int(i)
            return tmp
        return int(numbers)

    return 0
