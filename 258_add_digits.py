def addDigits(num: int) -> int:
    
    while num > 9:
        num = _crunch_num(num)

    return num

def _crunch_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    return sum

input = 38
print(addDigits(input))