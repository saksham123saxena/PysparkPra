from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("SamplingTransformation").getOrCreate()

rdd=spark.sparkContext.parallelize(range(100),4)

print("now of records in the provided rdd : "+str(rdd.count()))

for ele in rdd.top(7):
    print(ele)


## way of using sample transformation

# rdd.sample(withReplacement=False,fraction=0.1,seed=10).collect()
print("--------------")
rdd.sample(withReplacement=True,fraction=0.2,seed=13).collect()

## way of using takeSample action

print("--- using takeSample action -------")
# rdd_takeSample=rdd.takeSample(withReplacement=False,num=10,seed=17)


# print("type")
# print(type(rdd_takeSample))
#
# for ele in rdd_takeSample:
#     print(ele)
