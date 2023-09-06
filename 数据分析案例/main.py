"""
    面向对象，数据分析案例
"""

from file_define import JsonFileReader, TextFileReader, FileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
    text_data: list[Record] = text_file_reader.read_data()
    json_data: list[Record] = json_file_reader.read_data()

    # 将两个月份的数据合并为一个list
    all_data: list[Record] = text_data + json_data

    data_dict = {}
    # 开始数据计算
    for record in all_data:
        if data_dict.get(record.date):
            data_dict[record.date] += record.money
        else:
            data_dict[record.date] = record.money

    # 可视化图标的开发
    bar = Bar(init_opts=InitOpts(theme =ThemeType.LIGHT))
    bar.add_xaxis(list(data_dict.keys()))
    bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))

    bar.set_global_opts(
        title_opts=TitleOpts(title="2011年1-2月销售数据"),
    )
    bar.render("销售额.html")
