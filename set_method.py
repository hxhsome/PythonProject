"""
    集合
"""


def operation():
    set1 = {1, 2, 3}
    set2 = {1, 5, 6}
    # 求set1和set的差集，不会修改set1和set2里面的值，之后产生一个新集合
    # 也就是set1里面有的，但set2里面没有的
    difference = set1.difference(set2)
    print(f'消除差集后， 集合1结果：{set1}')
    print(f'消除差集后， 集合2结果：{set2}')
    print(f'消除差集后， 集合difference结果：{difference}')

    set1 = {1, 2, 3}
    set2 = {1, 5, 6}
    # 求set1和set的差集，会修改set1里面的值
    set1.difference_update(set2)
    print(f'消除差集后， 集合1结果：{set1}')
    print(f'消除差集后， 集合2结果：{set2}')

    set1 = {1, 2, 3}
    set2 = {1, 5, 6}
    # 求set1和set的差集，会修改set1里面的值
    union = set1.union(set2)
    print(f'消除差集后， 集合1结果：{set1}')
    print(f'消除差集后， 集合2结果：{set2}')
    print(f'消除差集后， 集合 union 结果：{union}')


def count_set():
    set1 = {1, 2, 3}
    set2 = {1, 5, 6, 3, 5, 7}
    print(f'set1 集合的长度为: {len(set1)}')
    print(f'set2 集合的长度为: {len(set2)}')


def for_set():
    set1 = {1, 5, 6, 3, 5, 7}
    for ele in set1:
        print(f'集合的元素有: {ele}')


if __name__ == '__main__':
    operation()
    count_set()
    for_set()
