"""

"""

from pyspark import SparkConf, SparkContext


def init_spark():
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

    sc = SparkContext(conf=conf)
    print(sc.version)

    sc.stop()


def spark2():
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
    sc = SparkContext(conf=conf)
    # 将python对象转成spark对象rdd
    rdd1 = sc.parallelize([1, 2, 3, 4, 5])
    rdd2 = sc.parallelize((1, 2, 3, 4, 5))
    rdd3 = sc.parallelize("abcdefg")
    rdd4 = sc.parallelize({1, 2, 3, 4, 5})
    rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

    # 读取文件内容
    rdd = sc.textFile("2011年1月销售数据.txt")
    print(rdd.collect())

    print(rdd1.collect())
    print(rdd2.collect())
    print(rdd3.collect())
    print(rdd4.collect())
    print(rdd5.collect())
    sc.stop()


if __name__ == '__main__':
    spark2()
