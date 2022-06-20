from pyspark.sql import SparkSession


class GetSparkSession:

    def get_spark_session(env_name,app_name):
            spark = SparkSession.builder.master(env_name) \
                .appName(app_name) \
                .getOrCreate()





