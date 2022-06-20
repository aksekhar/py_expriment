from pyspark.sql import SparkSession


class GetSparkSession:

   spark = SparkSession.builder.master('local') \
            .appName('appName') \
            .getOrCreate()
   print(spark)
