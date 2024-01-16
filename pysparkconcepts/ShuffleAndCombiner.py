from pyspark import SparkSession
spark=SparkSession.builder.master("local").appName("ShuffleAndCombiner").getOrCreate()

rdd=spark.sparkContext.parallelize([1,2,3])
print(rdd.toDebugString())
print("=====================")
rdd=rdd.distinct()
print(rdd.toDebugString())
