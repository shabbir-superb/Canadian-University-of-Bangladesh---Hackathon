"""
Palindrome Checker Solution
Checks if a given string is a palindrome (reads the same backward as forward).
Ignores non-alphanumeric characters and is case-insensitive.
"""

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f'"{test}" -> {result}')
