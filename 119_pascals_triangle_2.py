from typing import List

def getRow(rowIndex: int) -> List[int]:
    triangle = [[]] * (rowIndex  + 1)

    for n in range(rowIndex  + 1):
        triangle[n] = [1] * (n + 1)

        if n > 1:
            for m in range(n + 1):
                if m != 0 and m != n:
                    triangle[n][m] = triangle[n - 1][m - 1] + triangle[n - 1][m]

    return triangle[rowIndex]

print(getRow(3))