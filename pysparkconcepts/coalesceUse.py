from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("UseOfCoalesce").getOrCreate()

'''
df=spark.range(100000)
df=df.select(df.id,df.id*2,df.id*3)
df=df.union(df)
df=df.union(df)
df=df.union(df)
df=df.union(df)
df=df.union(df)
rdd=df.rdd.map(lambda x : str(x[0])+ ',' +str(x[1])+ ',' +str(x[2]))
for ele in rdd.top(10):
    print(ele)
'''
df=spark.range(10000)
print(type(df))
df.show(10)
df.printSchema()
print("total number of records "+str(df.count()))

rdd=df.rdd.map(lambda x:str(x[0]))

for ele in rdd.top(10):
    print(ele)

print("number of partitions are "+str(rdd.getNumPartitions()))
rdd=rdd.repartition(3)
print("number of partitions are "+str(rdd.getNumPartitions()))

# rdd.saveAsTextFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/coalesce1/")

# rdd.saveAsTextFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/coalesce2/",compressionCodecClass='org.apache.hadoop.io.compress.SnappyCodec')


## saving rdd records sequence formate



rdd.map(lambda x: (None, x)).saveAsSequenceFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/coalescesequence_1")
