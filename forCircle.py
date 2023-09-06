"""
    for循环
    for x in xxx 将xxx字符串中的一个个取出
"""


def for_in():
    name = 'hxhUltrapower'
    for x in name:
        print(x, end=' ')


def for_range():
    arr = [1, 2, 3, 4]
    # 从0到5，不包括5
    for a in range(5):
        print(a, end=' ')
    # 从1到5，不包括5
    for a in range(1, 5):
        print(a, end=' ')
    # 从1到5，不包括5，步长为2
    for a in range(1, 5, 2):
        print(a, end=' ')


def print9_9(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}', end='\t')
        print()


if __name__ == '__main__':
    for_in()
    for_range()
    print9_9(9)
