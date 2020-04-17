from random import Random
import re

def random_username():
    username = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(0,10):
        username +=chars[random.randint(0, length)]
    print(username)
    return username

if __name__ == "__main__":
    n = 3000
    while n > 0:
        random_username()
        n = n-1
