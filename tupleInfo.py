"""
    元组
        可以存储多个不同类型的元素
        内容不可以被修改
        变量名称 = ()
        变量名称 = tuple()
"""


def tuple_definition():
    t1 = (1, "Hello", True)
    print(f't1:{t1}')
    t2 = ()
    print(f't2:{t2}')
    t3 = tuple()
    print(f't3:{t3}')
    # t4 = tuple(1, "Hello", True)
    # print(f't4:{t4}')
    # 定义单个元组,需要在后面单独加个逗号
    t4 = ("hello")
    print(f't4的类型是:{type(t4)},内容为:{t4}')
    t4 = ("hello",)
    print(f't4的类型是:{type(t4)},内容为:{t4}')
    # 元组的嵌套
    t5 = ((1, 2, 3), (4, 5, 6))
    print(t5[1][2])


if __name__ == '__main__':
    tuple_definition()
    print('==========================================')
