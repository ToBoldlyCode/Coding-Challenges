def palindrome_substring(input_string):
    return input_string[1:-1]

def is_palindrome(input_string):
    if len(input_string) < 2:
        return True
    elif input_string[0] != input_string[-1]:
        return False
    else:
        return is_palindrome(palindrome_substring(input_string))