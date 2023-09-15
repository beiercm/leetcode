def digitSum(s: str, k: int) -> str:

    while len(s) > k:
        s = _crunch_str(s, k)

    return s

def _crunch_str(s, k):
    l = list(s)
    return_s = []
    while l:

        sum = 0
        for n in range(k):
            try:
                sum += int(l.pop(0))
            except IndexError as e:
                pass
        return_s.append(sum)

    return ''.join(map(str, return_s))

input = "11111222223"
k = 3
print(digitSum(input, k))