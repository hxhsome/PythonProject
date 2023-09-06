"""
    echarts
"""
import json
import pyecharts
from pyecharts.charts import Line, Map, Bar, Timeline
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
from pyecharts.globals import ThemeType


def base_line(x_data=["中国", "美国", "英国"], y_datas=[30, 20, 10], render_name="line.html"):
    # 创建一个折线图对象
    line = Line()
    # 给折线图对象添加X轴的数据
    line.add_xaxis(x_data)
    # 给折线图对象添加Y轴的数据
    for y_data in y_datas:
        line.add_yaxis("GDP", y_data)

    # 设置全局配置项
    line.set_global_opts(
        title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True)
    )

    line.render(render_name)


def america():
    f_us = open("美国.txt", "r", encoding="UTF-8")
    us_data = f_us.read()
    us_data = us_data.replace("jsonp_1629344292311_69436(", "")
    us_data = us_data[:-2]
    us_dict = json.loads(us_data)
    # print(type(us_dict))
    # print(us_dict)
    trend_data = us_dict['data'][0]['trend']
    x_data = trend_data['updateDate']
    x_data = x_data[:314]
    # print(x_data)
    y_data = trend_data['list'][0]['data']
    y_data = y_data[:314]
    f_us.close()
    return x_data, y_data


def india():
    f_us = open("印度.txt", "r", encoding="UTF-8")
    us_data = f_us.read()
    us_data = us_data.replace("jsonp_1629350745930_63180(", "")
    us_data = us_data[:-2]
    us_dict = json.loads(us_data)
    # print(type(us_dict))
    # print(us_dict)
    trend_data = us_dict['data'][0]['trend']
    x_data = trend_data['updateDate']
    x_data = x_data[:314]
    # print(x_data)
    y_data = trend_data['list'][0]['data']
    y_data = y_data[:314]
    f_us.close()
    return x_data, y_data


def japan():
    f_us = open("日本.txt", "r", encoding="UTF-8")
    us_data = f_us.read()
    us_data = us_data.replace("jsonp_1629350871167_29498(", "")
    us_data = us_data[:-2]
    us_dict = json.loads(us_data)
    # print(type(us_dict))
    # print(us_dict)
    trend_data = us_dict['data'][0]['trend']
    x_data = trend_data['updateDate']
    x_data = x_data[:314]
    # print(x_data)
    y_data = trend_data['list'][0]['data']
    y_data = y_data[:314]
    f_us.close()
    return x_data, y_data


def table(x_data, y_datas):
    y_label = ["美国确诊人数", "日本确诊人数", "印度确诊人数"]
    line = Line()
    line.add_xaxis(x_data)
    for idx in range(3):
        line.add_yaxis(y_label[idx], y_datas[idx], label_opts=LabelOpts(is_show=False))
        # line.add_yaxis(y_label[idx], y_datas[idx])
    line.render("yiqing.html")


def yiqing_map():
    f = open("疫情.txt", "r", encoding="UTF-8")
    data = f.read()
    f.close()
    data_dict = json.loads(data)
    province_data_list = data_dict['areaTree'][0]['children']
    data_list = []  # 绘图需要用的数据列表
    for province_data in province_data_list:
        province_name = province_data["name"]  # 省份名称
        province_confirm = province_data["total"]["confirm"]  # 确诊人数
        data_list.append((province_name, province_confirm))
    print(data_list)

    map = Map()

    map.add("各省份确诊人数", data_list, "china")

    map.set_global_opts(
        title_opts=TitleOpts(title="全国疫情地图"),
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,  # 是否分段
            pieces=[
                {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
                {"min": 100, "max": 999, "label": "100~999人", "color": "#FFFF99"},
                {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
                {"min": 5000, "max": 9999, "label": "5000~9999人", "color": "#FF6666"},
                {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#CC3333"},
                {"min": 100000, "label": "100000+", "color": "#990033"},
            ]
        )
    )
    map.render("全国疫情地图.html")


def bar_method():
    bar = Bar()

    bar.add_xaxis(["中国", "美国", "英国"])

    bar.add_yaxis("GDP", [30, 20, 10],
                  label_opts=LabelOpts(position="right"))

    # 反转xy轴
    bar.reversal_axis()
    bar.render("基础柱状图.html")


def bar_timeline():
    bar1 = Bar()
    bar1.add_xaxis(["中国", "美国", "英国"])
    bar1.add_yaxis("GDP", [30, 20, 10],
                   label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar1.reversal_axis()

    bar2 = Bar()
    bar2.add_xaxis(["中国", "美国", "英国"])
    bar2.add_yaxis("GDP", [40, 10, 20],
                   label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar2.reversal_axis()

    bar3 = Bar()
    bar3.add_xaxis(["中国", "美国", "英国"])
    bar3.add_yaxis("GDP", [70, 50, 60],
                   label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar3.reversal_axis()

    timeline = Timeline(
        {"theme": ThemeType.LIGHT}
    )

    # timeline = Timeline()
    timeline.add(bar1, "点1")
    timeline.add(bar2, "点2")
    timeline.add(bar3, "点3")

    timeline.add_schema(
        play_interval=1000,  # 自动播放时间，单位：毫秒
        is_timeline_show=True,  # 是否显示时间线
        is_auto_play=True,  # 是否自动播放
        is_loop_play=True  # 是否循环播放
    )



    timeline.render("时间线柱状图.html")


if __name__ == '__main__':
    # base_line()

    # a_x_data, a_y_data = america()
    # i_x_data, i_y_data = india()
    # j_x_data, j_y_data = japan()
    # table(a_x_data, [a_y_data, i_y_data, j_y_data])

    # yiqing_map()

    # bar_method()

    bar_timeline()
