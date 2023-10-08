from pyspark.sql import SparkSession
spark=SparkSession\
    .builder\
    .master("local")\
    .appName("dataframes")\
    .getOrCreate()


rdd=spark.sparkContext.parallelize([1,2,3,4])
for e in rdd.collect():
    print(e)
