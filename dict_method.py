"""
    字典
"""


def definition():
    dict1 = {"key1": "value1", "key2": 23, "key3": (1, 2, 3)}
    print(f'dict1:{dict1},类型为:{type(dict1)}')
    # 定义空的
    # 这里{}可以用来定义集合，但是定义空集合是set() {}是用来定义空dict
    dict2 = {}
    print(f'dict2:{dict2},类型为:{type(dict2)}')
    dict3 = dict()
    print(f'dict3:{dict3},类型为:{type(dict3)}')


def get_value_by_key():
    dict1 = {"key1": "value1", "key2": 23, "key3": (1, 2, 3)}
    print(f'dict1:key1:{dict1["key1"]}')
    print(f'dict1:key1:{dict1.get("key1")}')
    # []取，没有会报错
    # print(f'dict1:keyNone:{dict1["keyNone"]}')
    print(f'dict1:key1:{dict1.get("keyNone")}')


def dict_for():
    dict1 = {"key1": "value1", "key2": 23, "key3": (1, 2, 3)}
    for key in dict1:
        print(f'key:{key},value:{dict1[key]}')


if __name__ == '__main__':
    definition()
    print("============")
    get_value_by_key()
    print("============")
    dict_for()
