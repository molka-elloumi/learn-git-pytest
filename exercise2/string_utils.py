# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    cleaned = ''.join(s.lower().split())  # Remove spaces and convert to lowercase
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    return s.title()
#testing
#choose random word to test the function each time for this case we chose hello , python and A man a plan a canal Panama (had to look up palindromes)
print("Reverse String Tests:")
print(reverse_string("hello"))  
print(reverse_string("Python"))  
print(reverse_string("")) 

print("Count Vowels Tests:")
print(count_vowels("hello"))  
print(count_vowels("PYTHON"))  
print(count_vowels("AEIOU"))  
print(count_vowels("bcdfg"))

print("\nIs Palindrome Tests:")
print(is_palindrome("racecar"))  
print(is_palindrome("Hello"))  
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("123321"))  
print(is_palindrome("Python"))  

print("\nCapitalize Words Tests:")
print(capitalize_words("hello world"))  
print(capitalize_words("PYTHON programming"))  
print(capitalize_words("123 abc"))  
print(capitalize_words(""))  
