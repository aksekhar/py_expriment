from common.get_spark_session import GetSparkSession


if __name__ == '__main__':
    print('load params')

    spark = GetSparkSession.get_session()
    print(spark)


