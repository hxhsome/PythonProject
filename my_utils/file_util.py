"""
    文件处理相关工具
"""


def print_file_info(file_name):
    file = None
    try:
        file = open(file_name, 'r', encoding="utf-8")
        content = file.read()
        print(f'文件的所有内容如下：\n {content}')
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()


def append_to_file(file_name, data):
    """
    将指定的数据追加到指定的文件中
    :param file_name: 执行文件的路径
    :param data: 指定的数据
    :return: None
    """
    file = open(file_name, mode='a', encoding='utf-8')
    file.write(data)
    file.write('\n')
    file.close()


if __name__ == '__main__':
    append_to_file('a.txt', "hxh")
    print_file_info('a.txt')
