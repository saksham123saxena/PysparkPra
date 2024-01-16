from pyspark import SparkSession
from operator import add

spark=SparkSession\
    .builder\
    .master("local")\
    .appName("ReduceByKey")\
    .getOrCreate()

rdd=spark.sparkContext.parallelize([("a",1),("a",1),("c",1)])
rddAns=rdd.reduceByKey(add)
for x in rddAns.collect():
    print(x)

rddGroupByKey=rdd.groupByKey()
rddGroupByKeyIterable=rddGroupByKey.map(lambda x: (x[0],sum(x[1])))

for x in rddGroupByKeyIterable.collect():
    print(x)

