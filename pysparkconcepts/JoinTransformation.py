from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("JoinTransformation").getOrCreate()

order=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orderitem.txt")

orderItem=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orders.txt")

for ele in order.collect():
    print(ele)

for ele in orderItem.collect():
    print(ele)

order1=order.map(lambda x : (x.split(',')[0],x.split(',')[2]))
for ele in order1.collect():
    print(ele)
orderItem1=orderItem.map(lambda x : (x.split(',')[0],x.split(',')[4]))
for ele in orderItem1.collect():
    print(ele)

## applying the join
join=order1.join(orderItem1)

for ele in join.collect():
    print(ele)

# for modification of join result
join1=order1.join(orderItem1).map(lambda x : x[1][0]+ " - "+x[1][1])

for ele in join1.collect():
    print(ele)

print(type(join1))
