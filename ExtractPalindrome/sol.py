def solution(s):
    
    def prefixPalindromeCheck(s, start, end):

        if start == end:
            return ''
        
        for e in range(end, start +1, -1):
            if s[start:e] == s[start:e][::-1]:
                return prefixPalindromeCheck(s, e, end)
        return s[start:]
    return prefixPalindromeCheck (s, 0, len(s))

""" You are given a string s. Consider the following algorithm applied to this string:

    Take all the prefixes of the string, and choose the longest palindrome between them.
    If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.

Your task is to implement the above algorithm and return its result when applied to string s. """