"""
    json
"""

import json


def init_data():
    data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
    json_str = json.dumps(data, ensure_ascii=False)
    print(type(json_str))
    print(json_str)


def init_dict():
    data = {"name": "周杰伦", "addr": "台北"}
    json_str = json.dumps(data, ensure_ascii=False)
    print(type(json_str))
    print(json_str)


def str_to_list():
    str = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
    l = json.loads(str)
    print(type(l))
    print(l)


def str_to_dict():
    str = '{"name": "周杰伦", "addr": "台北"}'
    d = json.loads(str)
    print(type(d))
    print(d)



if __name__ == '__main__':
    # init_data()
    # init_dict()
    # str_to_list()
    # str_to_dict()
