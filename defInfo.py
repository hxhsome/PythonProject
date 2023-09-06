"""
    无返回值，返回的是None
    if判断中 None等同于False
"""


def return_void():
    """
    为了判断什么都不返回，是否与return None等价
    :return: 无任何返回值
    """
    print("没有任何返回值")


def return_none():
    print("返回值为None")
    return None


if __name__ == '__main__':
    print(type(return_void()))
    return_none_value = return_none()
    print(type(return_none_value))
    if return_none_value:
        print('return_none_value is True')
    else:
        print('return_none_value is False')
