from time import time

from pyspark import SparkSession
spark=SparkSession.builder.master("local").appName("CalculatingSpeedOfSpark").getOrCreate()

def speedCal():
    st=time()
    print("starting time "+str(st))
    kk=spark.range(1000 * 1000 * 1000)
    en=time()
    df=en-st
    print(df)


print("Calculating The Speed of Spark!!")
# speedCal()
# print(str(time()))
df=spark.range(1000).filter("id>100").selectExpr("sum(id)").show()
print(type(df))
n1=1000
n2=100
print((n1*(n1+1))/2)
print((n2*(n2+1))/2)
d1=(n1*(n1+1))/2
d2=(n2*(n2+1))/2
print(d2-d1)

df1=spark.range(10000)
df1.printSchema()
spark.range(1000).filter("id>100").selectExpr("sum(id)").explain()

print("For printing everything !!")
spark.range(1000).filter("id>100").selectExpr("sum(id)").explain(extended=True)
'''
101----1000
(1----1000)-(1----100)= 500500-5050=
'''
