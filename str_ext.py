"""
    字符串的扩展，字符串的拼接
"""
if __name__ == '__main__':
    # 单引号定义法
    name = 'hxh'
    # 双引号定义法
    name = "hxh"

    name = """多双引号定义法"""

    print(name)
    name = 'hxh'
    gender = '男'
    print("我是", name + "，我的性别是:", gender)

    print("我是%s,我%%的性别是:%s,%5d,%.2f" % (name, gender, 1, 13.14))
    print("我是{},我的性别是:{}".format(name, gender))
    print(f'我是{name},我的性别是:{gender}')

