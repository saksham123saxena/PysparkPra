from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("UseOfCountByKey").getOrCreate()

rdd=spark.sparkContext.parallelize([("deliverd",1),("pending",2),("on_going",3),
                                    ("deliverd",1),("pending",2),("on_going",3),
                                    ("deliverd",1),("pending",2),("on_going",3),
                                    ("deliverd",1),("pending",2),("on_going",3)])

for ele in rdd.collect():
    print(ele)

count_agg_rdd=rdd.countByKey()
print(type(count_agg_rdd))
for ele in count_agg_rdd.items():
    print(ele)
