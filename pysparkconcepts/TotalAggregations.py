from pyspark import SparkSession
from operator import add

spark=SparkSession.builder.master("local").appName("AllAggretationOperation").getOrCreate()

rdd=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orderitem.txt")
rdd1=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/orders.txt")

for ele in rdd.collect():
    print(ele)

print(rdd.count())

## calculating total Closed order
ans=rdd.filter(lambda x:x.split(',')[3]=="CLOSED").count()
print("total closed order : "+str(ans))

## way of using reduce

for ele in rdd1.collect():
    print(ele)

ans1=rdd1.filter(lambda x : int(x.split(',')[2])<=1000)\
    .map(lambda x :int(x.split(',')[2])).reduce(lambda a,b : (a+b))
## we can using add function for achieving above result
ans2=rdd1.filter(lambda x : int(x.split(',')[2])<=1000)\
    .map(lambda x:int(x.split(',')[2])).reduce(add)

print("final sum of provided RDD1 "+str(ans1) +"  "+str(ans2))

## find out the maximum sub amount from rdd1
ans3=rdd1.reduce(lambda a,b: a if float(a.split(',')[4]) > float(b.split(',')[4]) else b)
print("maximum sub amount  "+str(ans3))

ans3=rdd1.map(lambda x:float(x.split(',')[4])).reduce(max)
print("maximum sub amount MAX  "+str(ans3))


## for smallest
ans4=rdd1.reduce(lambda a,b: a if float(a.split(',')[4]) < float(b.split(',')[4]) else b)
print("maximum sub amount  "+str(ans4))
ans4=rdd1.map(lambda x:float(x.split(',')[4])).reduce(min)
print("maximum sub amount MIN "+str(ans4))
