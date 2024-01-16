from pyspark import SparkSession

spark=SparkSession.builder.master("local").appName("GroupByKey").getOrCreate()

df=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orderitem.txt")
for x in df.collect():
    print(x)

dateGroup=df.map(lambda x : (x.split(',')[1],int(x.split(',')[2]))).groupByKey()


for i in dateGroup.mapValues(sum).collect():
    print(i)


dateGroup1=dateGroup.map(lambda x : (x[0],sum(x[1])))

for x in dateGroup1.collect():
    print(x)


'''
skdms
'''

