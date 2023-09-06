"""
    数据定义的类
"""


class Record:
    def __init__(self, date, order_id, money, province):
        """

        :param date: 订单日期
        :param order_id: 订单ID
        :param money: 订单金额
        :param province: 销售省份
        """
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f'date:{self.date}, order_id: {self.order_id}, money: {self.money}, province: {self.province}'


if __name__ == '__main__':
    record = Record('2022-12-12', '123123', 123123, '山东')
    print(record)
