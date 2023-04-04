def solution(numbers):
    def swap_largest_digit(number):
        num_str = str(number)
        max_digit = max(num_str)
        for i, digit in enumerate(num_str):
            if digit == max_digit:
                break
        return int(num_str[:i] + num_str[i + 1:] + max_digit)

    def is_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            swapped_i = swap_largest_digit(numbers[i])
            swapped_next = swap_largest_digit(numbers[i + 1])
            temp_i = numbers[i]
            temp_next = numbers[i + 1]

            numbers[i] = swapped_i
            if is_increasing(numbers):
                return True
            numbers[i] = temp_i

            numbers[i + 1] = swapped_next
            if is_increasing(numbers):
                return True
            numbers[i + 1] = temp_next

            return False

    return True

#current solution only passed 18/20 test cases; 8/10 hidden test cases

""" You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

Example

    For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.

    The initial array is already strictly increasing, so no actions are required.

    For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.

    By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

    For numbers = [13, 31, 30], the output should be solution(numbers) = false.
        The initial array elements are not increasing.
        By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
        By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
        By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;

    So, it's not possible to obtain a strictly increasing array, and the answer is false.
"""