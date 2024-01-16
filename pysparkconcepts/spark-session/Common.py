from pyspark import SparkSession
spark=SparkSession\
    .builder\
    .master("local")\
    .appName("SparkContextForCommon")\
    .getOrCreate()
