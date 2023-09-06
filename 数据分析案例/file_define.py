"""
    和文件相关的类定义
"""
import json

from data_define import Record


# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件路径

    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path


    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    # text_file_reader = TextFileReader("2011年1月销售数据.txt")
    # text_file_reader.read_data()
    json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
    data = json_file_reader.read_data()
    for record in data:
        print(record)
