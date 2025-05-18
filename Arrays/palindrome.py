'''
Problem:

Given a string s, return true if it is a palindrome, or false otherwise.
An integer is a palindrome when it reads the same backward as forward.
An integer x is a palindrome when reverse(x) == x.  

'''

def isPalindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    Args:
    s (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    if isinstance(s,str):
        j = len(s) - 1
        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -= 1
    else:
        return Exception("Invalid input, your function input must be a string")
    
print(isPalindrome("Hello"))