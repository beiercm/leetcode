def twoSum(numbers, target):
    start_index = 0
    end_index = len(numbers) - 1

    while start_index < end_index:
        sum = numbers[start_index] + numbers[end_index]

        if sum == target:
            return [start_index + 1, end_index + 1]

        if sum < target:
            start_index += 1

        if sum > target:
            end_index -= 1


_input = [2, 7, 11, 15]
target = 9
print(twoSum(_input, target))