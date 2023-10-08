from pyspark.sql import SparkSession

def lowerCaseConverter(str):
    return str.lower()

spark=SparkSession\
    .builder\
    .master("local")\
    .appName("RDD-OPERATION")\
    .getOrCreate()

rdd=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orderitem.txt")
rdd1=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orders.txt")


for ele in rdd.collect():
    print(ele)


print("list of the orders items")
for ele in rdd1.collect():
    print(ele)

"""
# map-transformation

odrMap=rdd.map(lambda x : (x.split(',')[0],x.split(',')[3]))

ordMap1=rdd.map(lambda x : x.split(',')[0]+'#'+x.split(',')[3])

for e in ordMap1.collect():
    print(e)

odrdate=rdd.map(lambda x : x.split(',')[1].split(' ')[0].replace('-','/'))

for e in odrdate.collect():
    print(e)

## creating key-value pair
odrKeyValue=rdd.map(lambda x : (x.split(',')[0],x))

for x in odrKeyValue.collect():
    print(x)

## getting the order-id and money of orderitem from rdd1
orderItem=rdd1.map(lambda x : (x.split(',')[0],x.split(',')[4]))

for ele in orderItem.collect():
    print(ele)

# creating the user-define-function converting the status into lowercase
odrStatus=rdd.map(lambda x : lowerCaseConverter(x.split(',')[3]))
for e in odrStatus.collect():
    print(e)

print(lowerCaseConverter("SPARK"))

"""

"""

## flatmap tranformation [it flattes the results based on the required inputs]
odr1=rdd.flatMap(lambda x : x.split(','))
wordAssigned=odr1.map(lambda x : (x,1))
# aggregating the results
wordCount=wordAssigned.reduceByKey(lambda x,y : x+y)
for e in wordCount.collect():
    print(e)

# print("=========== another way of printing ================")
# ## alternative way of writing above code logic
# wordCount1=rdd.flatMap(lambda x : x.split(',')).map(lambda z : (z,1)).reduceByKey(lambda a,b : a+b)
# for k in wordCount1.collect():
#     print(k)

"""

"""
## filter transformation

filterResult=rdd.filter(lambda x: ((x.split(',')[3]=="CLOSED") or (x.split(',')[3]=="COMPLETE")
                                   and (x.split(',')[1].split('-')[0] == '2013')) )
for e in filterResult.collect():
    print(e)

"""

##mapValue transformation

rdd2=spark.sparkContext.parallelize([("a",[1]),("b",[1,2]),("c",[1,2,3])])
ans=rdd2.mapValues(len)
for ele in ans.collect():
    print(ele)
