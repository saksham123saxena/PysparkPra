from pyspark import SparkSession
# from pyspark.sql.types import StructType,StructField, StringType
from pyspark import StructType,StructField, LongType
spark=SparkSession.builder.master("local").appName("GroupByKey").getOrCreate()
'''
deptSchema = StructType([       
    StructField('dept_name', StringType(), True),
    StructField('dept_id', StringType(), True)
])

deptDF1 = spark.createDataFrame(rdd, schema = deptSchema)
deptDF1.printSchema()
deptDF1.show(truncate=False)

'''


# df=spark.read.parquet("/tmp/iceberg/datalake/user_ops_data_v4_temp1/data/*")
print("hello ")
rdd=spark.sparkContext.parallelize([1654415586,1698933208])

dept = StructType([
    StructField('date',LongType(),True)
])

df=spark.createDataFrame(rdd, schema = dept)
for ele in rdd.collect():
    print(ele)

# df.show()
print(df.printSchema())

