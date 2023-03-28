def solution(s):
    
    def prefixPalindromeCheck(s, i, j):

        if i == j:
            return ''
        
        for e in range(j, i +1, -1):
            if s[i:e] == s[i:e][::-1]:
                return prefixPalindromeCheck(s, e, j)
        return s[i:]
    return prefixPalindromeCheck (s, 0, len(s))

#OR

#only passed 4 test cases
def longest_palindrome_prefix(s):
    while len(s) > 1:
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                if i < len(s):
                    s = s[i:]
                    break
                else:
                    return s
    return s



""" You are given a string s. Consider the following algorithm applied to this string:

    Take all the prefixes of the string, and choose the longest palindrome between them.
    If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, j the algorithm with the current string s as a result.

Your task is to implement the above algorithm and return its result when applied to string s. """