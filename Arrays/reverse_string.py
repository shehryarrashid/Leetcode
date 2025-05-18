'''
 
 Given a string as input return this reversed

 Example: ['h', 'e', 'l', 'l', 'o'] -> ['o', 'l', 'l', 'e', 'h']

 '''

# Easy output

def reverse_string(s: str) -> str:
    output = ""
    i = len(s) - 1

    while i >= 0:
        output += s[i]
        i -= 1

    return output

# Efficient way

def reverse_string(s: str) -> str:
    s = list(s)  # Convert string to list for mutability
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap
        left += 1
        right -= 1

    return ''.join(s)  # Convert list back to string


print(reverse_string("hello"))