from pyspark import SparkSession

spark=SparkSession.builder.master("local").appName("Set-Transformation").getOrCreate()

rdd1=spark.sparkContext.parallelize(("1","2","3","4"))

for ele in rdd1.collect():
    print(ele)


rdd2=spark.sparkContext.parallelize(("5","6","7","8","1","2"))

for ele in rdd2.collect():
    print(ele)

rdd_union=rdd2.union(rdd1)
print("union result")
for ele in rdd_union.collect():
    print(ele)

print("intersection result")

rdd_intersection=rdd2.intersection(rdd1)

for ele in rdd_intersection.collect():
    print(ele)


print("distinct use ")

rdd_distinct_ans=rdd_union.distinct()

for ele in rdd_distinct_ans.collect():
    print(ele)

print("use of subtract set transformation")

rdd_subtract_ans=rdd2.subtract(rdd1)

for ele in rdd_subtract_ans.collect():
    print(ele)
