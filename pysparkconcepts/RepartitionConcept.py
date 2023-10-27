from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("UseOfRepartition").getOrCreate()
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
## saving above rdd in location without partition

# rdd.saveAsTextFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/patition1/")
# rdd.coalesce(1).saveAsTextFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/patition2/")

# print("number of partition "+str(rdd.getNumPartitions()))  ## getting the number of partition = 6
#
# rdd=rdd.coalesce(1)
#
# print("number of partition "+str(rdd.getNumPartitions()))  ## getting the number of partition =1
#


## getting the number of partition
print("number of partition "+str(rdd.getNumPartitions()))

## getting the number of records in every partition
li=rdd.glom().map(len).collect()
print("type of li "+str(type(li)))

## printing the number of element in each parition
num=0
for ele in li:
    print(str(num)+" -- "+str(ele))
    num=num+1

## now, i am decreasing the number of partitions
rdd=rdd.repartition(4)

print("after decreasing the partition--------")
print("number of partition "+str(rdd.getNumPartitions()))

li1=rdd.glom().map(len).collect()

num1=0
for ele in li1:
    print(str(num1)+" -- "+str(ele))
    num1=num1+1

