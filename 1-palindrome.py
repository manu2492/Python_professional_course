

def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    if string == string[::-1]:
        return True
    else:
        return False


def run():
    print(is_palindrome('Ana'))


if __name__ == '__main__':
    run()
