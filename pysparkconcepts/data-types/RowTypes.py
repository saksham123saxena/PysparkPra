from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *
spark=SparkSession\
    .builder\
    .master("local")\
    .appName("RowTypeDataType")\
    .getOrCreate()
# Row class object
'''
data=Row(name="hello",time=1)
print(data)
print(type(data))
print(data.name)
print(data.time)
print('hello' in data.name)

print("creating rdd via row object!!")
l=[Row(name="hello",time=1),
   Row(name="hello2",time=2),
   Row(name="hello3",time=3)]

rdd=spark.sparkContext.parallelize(l)

print("printing the element of rdd!!")

for ele in rdd.collect():
    print(ele)

print("creating dataframe from rdd!!")
df=spark.createDataFrame(rdd)
df.printSchema()
df.show()

'''

# print("now, will use custom row class!!")
# Person=Row("name","age") # here, entities are fixed
# p1=Person("hello1",1)
# p2=Person("hello2",2)
# print(p1)
# print(type(p2))
#
# l=[p1,p2]
# rdd=spark.sparkContext.parallelize(l)
# print("printing the values of rdd!!")
# for ele in rdd.collect():
#     print(ele)
#
# print("creating the dataframe")
# #df=spark.createDataFrame(rdd)
# sh=StructType([
#     StructField('name',StringType(),True),
#     StructField('time',IntegerType(),True)
# ])
# df=spark.createDataFrame(rdd,schema=sh)
# df.printSchema()
# df.show()


import os
import sys
print(os.path.dirname(sys.executable))
