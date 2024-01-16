import Common as s
from pyspark import col,to_date


df=s.spark.read.load("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/input1.parquet",
                     format='parquet',inferSchema=True)
df.printSchema()
df.show(10)

df1 = df.withColumn("partition1", to_date(col("partition")))
df1.printSchema()
df1.show(10)
