'''

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.


'''

def is_subsequence(s: str, t : str) -> bool:
    i = j = 0

    while i < len(t):
        if s[j] == t[i]:
            j += 1
        i += 1
        
    return j == len(s)

print(is_subsequence("ace", "abcde"))