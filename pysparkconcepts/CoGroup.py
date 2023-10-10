from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("JoinTransformation").getOrCreate()

"""
r1=spark.sparkContext.parallelize([("a",1)])
r2=spark.sparkContext.parallelize([("a",1),("b",2)])

for e in r1.collect():
    print(e)

for e in r2.collect():
    print(e)

r1r2=r1.cogroup(r2)

for e in r1r2.collect():
    print(e)

print("iterating via map")
for i,j in r1r2.collect():
    print(i,map(list,j))

"""

## cartesian

rdd1=spark.sparkContext.parallelize([1,2,3])
rdd2=spark.sparkContext.parallelize([1,2,3])

r=rdd2.cartesian(rdd2)
for e in r.collect():
    print(e)

ans=sorted(r.collect(),reverse=True)

print(ans)
 
