from pyspark.sql import SparkSession

spark=SparkSession\
    .builder\
    .master("local")\
    .appName("RDDCREATIONWAYS")\
    .getOrCreate()


# from dataframe |
# df=spark.createDataFrame(data=[("robert",23),("rohan",21)],schema=['name','age'])
# df.printSchema()
# df.show()

# from extername source [will use gcs] |

# local data [via textFile]
# rdd1=spark.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/input2.txt")
# rdd1.count()

# from python list
li=["saksham","saxena",25,"PG","Emp of KOO INDIA"]
rdd2=spark.sparkContext.parallelize(li)
for ele in rdd2.collect():
    print(ele)

# from other rdd
rdd3=rdd2
print("-------another rdd -----------")

for ele in rdd3.collect():
    print(ele)
