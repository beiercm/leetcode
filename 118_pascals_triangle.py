from typing import List

def generate(numRows: int) -> List[List[int]]:
    triangle = [[]] * numRows

    for n in range(numRows):
        triangle[n] = [1] * (n + 1)

        if n > 1:
            for m in range(n + 1):
                if m != 0 and m != n:
                    triangle[n][m] = triangle[n - 1][m - 1] + triangle[n - 1][m]

    return triangle

print(generate(5))