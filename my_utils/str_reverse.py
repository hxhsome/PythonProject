"""
    字符串相关工具
"""


def str_reverse(s):
    return s[-1::-1]


def substr(s, x, y):
    return s[x:y]


if __name__ == '__main__':
    str = "123456789"
    reverse = str_reverse(str)
    print(f'reverse: {reverse}')
    substr1 = substr(str, 3, 5)
    print(f'substr1: {substr1}')
