from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("RepartitionAndSort").getOrCreate()

rdd=spark.sparkContext.parallelize(((1,('a','z')),(3,('b','y')),(4,('c','x')),(5,('d','w')),(6,('a','z'))
                                    ),2)

print("number of partition in given rdd "+str(rdd.getNumPartitions()))
##printing the parition element
print(rdd.glom().collect())
rdd1=rdd.repartitionAndSortWithinPartitions(2,lambda x:x%2,ascending=True)
print("printing element after the repartition and sorting")
print(rdd1.glom().collect())
