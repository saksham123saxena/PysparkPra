from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("BatchJobPipelines").getOrCreate()

df=spark.read.parquet("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/batchjob/2023-11-26/*/*")
df.printSchema()
print("total number of records "+str(df.count()))
spark.stop()


# //2923


# 257
# 1000   500
# 340
# 2000   1000
# 600
# 4000   2000
# 1259
# 8000   4000
# 2923
# 16000   8000
