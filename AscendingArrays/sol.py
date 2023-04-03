def solution(a):
    digit_count = {}
    
    for num in a:
        for digit in str(abs(num)): 
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
    
    max_count = max(digit_count.values())
    
    most_common = [int(digit) for digit in digit_count if digit_count[digit] == max_count]
    
    return sorted(most_common)
    
""" Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.
Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1

The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5]. """
