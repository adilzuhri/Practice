def solution(a, k):
    # initialize the remainder dictionary with 0s
    remainder = {}
    for i in range(k):
        remainder[i] = 0
    # count the number of remainders
    for i in range(len(a)):
        remainder[a[i] % k] += 1
    # calculate the number of pairs for each remainder
    result = 0
    for i in range(1, k//2+1):
        if i != k-i:
            result += remainder[i] * remainder[k-i]
        else:
            result += remainder[i] * (remainder[i]-1) // 2
    # add the pairs with remainder 0
    result += remainder[0] * (remainder[0]-1) // 2
    return result

#current solution passes 9/11 test cases. Program exceeded allowed memory limit.

""" You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two different indices i < j, such that a[i] + a[j] is divisible by k.

Example

For a = [1, 2, 3, 4, 5] and k = 3, the output should be solution(a, k) = 4.

There are 4 pairs of numbers that sum to a multiple of k = 3:

a[0] + a[1] = 1 + 2 = 3
a[0] + a[4] = 1 + 5 = 6
a[1] + a[3] = 2 + 4 = 6
a[3] + a[4] = 4 + 5 = 9
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of integers from which two numbers should be picked. The elements are not necessarily all unique.

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 109.

[input] integer k

An integer, which should be a divisor of the sum.

Guaranteed constraints:
1 ≤ k ≤ 109.

[output] integer64

The number of ways to pick two different numbers from a, such that their sum is divisible by k. """