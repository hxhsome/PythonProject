"""
pymysql库的基础操作
"""

from pymysql import Connection

if __name__ == '__main__':
    connection = Connection(host="localhost", user="hxh", password="hxh123", port=3306, autocommit=True)
    info = connection.get_host_info()
    print(info)

    cursor = connection.cursor()
    # 选择哪个数据库
    connection.select_db("book")
    # execute = cursor.execute("select * from book")
    # execute = cursor.execute("create table test_pymysql(id int)")
    # print(type(execute))
    # print(execute)

    # 执行SQL后，使用fetchall获取结果集
    cursor.execute("select * from book")
    result: tuple = cursor.fetchall()
    for r in result:
        print(r)

    cursor.execute("insert into test_pymysql(id) values(10)")
    # 需要commit才能使insert生效，或者创建connection对象的时候，使用autocommit=True
    # connection.commit()
    connection.close()
