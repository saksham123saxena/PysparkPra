from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("TakeOrderedTransformation").getOrCreate()

# rdd=spark.sparkContext.parallelize([11,3,1,4,5,7])
# for ele in rdd.collect():
#     print(ele)
#
# takeOr_rdd=rdd.takeOrdered(2)
# print(takeOr_rdd)  ## output: [1, 3]
#
# ## for getting the descending
# print(rdd.takeOrdered(3,key=lambda x:-x))
#
# ## for getting the ascending order
# print(rdd.takeOrdered(3,key=lambda x:x))

'''
Ranking : on the basis of the grou
'''
rdd=spark.sparkContext.parallelize([(1,"closed",123),
                                    (2,"complete",200),
                                    (12,"complete",200),
                                    (22,"complete",200),
                                    (3,"pending",300),
                                    (4,"complete",143),
                                    (5,"closed",500),
                                    (6,"pending",190)])
