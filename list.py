"""
    列表list
"""


def definition_list():
    params = [1, 2, 3]
    print(params)
    for p in params:
        print(p, end=' ')
    type_not_same = ['hxh', True, 123]
    print(type_not_same)
    for yns in type_not_same:
        print(yns, end=' ')
    list_list = [[1, 2, 3], [2, 3, 4]]
    print(list_list)
    for l in list_list:
        print(l, end=' ')
    for i in range(len(params)):
        print(params[i])
    for i in range(-1, -4, -1):
        print(params[i])


def index_use():
    params = [1, 2, 3]
    idx = params.index(1)
    print(idx)
    idx = params.__contains__(4)
    print(idx)
    params[2] = 4
    idx = params.__contains__(3)
    print(idx)
    params.insert(1, 6)
    print(params)


def list_crud():
    params = [1, 2, 3]
    params[2] = 4
    print(params)
    # 指定下标1查询某个元素6
    params.insert(1, 6)
    print(f'insert 方法后{params}')
    # 添加一个元素
    params.append(7)
    print(f'append 方法后{params}')
    # 添加一批元素
    params.extend([4, 5, 6])
    print(f'extend 方法后{params}')
    # 传入下标删除,不传删除最后一个，返回值为取出的值
    params.pop(0)
    print(f'pop方法后{params}')
    del params[len(params) - 1]
    print(f'del方法后{params}')
    # 传入元素值来删除元素
    params.remove(2)
    print(f'remove方法后{params}')
    cnt = params.count(6)
    print(f'count 传入某个元素，统计某个元素的个数 方法后的返回值：{cnt}')
    lcnt = len(params)
    print(f'len 函数 统计某个列表元素的个数 方法后的返回值：{lcnt}')
    params.clear()
    print(f'clear 方法后{params}')


def exec():
    exec_list = [21, 25, 21, 23, 22, 20]
    # 追加一个31
    exec_list.append(31)
    # 追加一个新的列表[29, 33, 30] 到列表的尾部
    exec_list.extend([29, 33, 30])
    # 取出第一个元素
    # exec_list.remove(21)
    exec_list[0]
    # 取出最后一个元素
    exec_list[-1]
    # 查找元素31在列表中的下标
    exec_list.index(31)


def list_while_func():
    """
    使用while循环遍历列表的演示代码
    :return: None
    """
    my_list = ['ultrapower', 'hxh', 'python']
    i = 0
    while i < len(my_list):
        ele = my_list[i]
        print(f'下标{i}的元素为:{ele}')
        i += 1


def list_for_func():
    """
    使用for循环遍历列表的演示代码
    :return: None
    """
    my_list = ['ultrapower', 'hxh', 'python']
    for i in range(len(my_list)):
        ele = my_list[i]
        print(f'下标{i}的元素为:{ele}')


def list_for_exec():
    my_list = []
    result_list = []
    for i in range(10):
        my_list.append(i)
    for ele in my_list:
        if ele % 2 == 0:
            result_list.append(ele)
    print(f'for循环得到的偶数数组为：{result_list}')


def list_while_exec():
    my_list = []
    result_list = []
    for i in range(10):
        my_list.append(i)
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            result_list.append(my_list[i])
        i += 1
    print(f'while 循环得到的偶数数组为：{result_list}')


if __name__ == '__main__':
    definition_list()
    print('==========================================')
    index_use()
    print('==========================================')
    list_crud()
    print('==========================================')
    list_while_func()
    print('==========================================')
    list_for_func()
    print('==========================================')
    list_for_exec()
    print('==========================================')
    list_while_exec()
