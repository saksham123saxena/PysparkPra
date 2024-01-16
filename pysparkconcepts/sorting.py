from pyspark import SparkSession

spark=SparkSession.builder.master("local").appName("SortingAPI").getOrCreate()

rdd=spark.sparkContext.parallelize([(1,"closed",123),
                                    (2,"complete",200),
                                    (12,"complete",200),
                                    (22,"complete",200),
                                    (3,"pending",300),
                                    (4,"complete",143),
                                    (5,"closed",500),
                                    (6,"pending",190)])

for ele in rdd.collect():
    print(ele)

## making the rdd in key-value pair form

rdd1=rdd.map(lambda x: (int(x[2]),x))
for x in rdd1.collect():
    print(x)

## now, apply the sorting transformation

sort_rdd=rdd1.sortByKey(ascending=True)

for ele in sort_rdd.collect():
    print(ele)


print("descending order of printing")
sort_rdd1=rdd1.sortByKey(ascending=False)

for ele in sort_rdd1.collect():
    print(ele)
