from pyspark import *

spark=SparkSession.builder.master("local").appName("DataTypesPysaprk").getOrCreate()

data=[('hello',0,{'hello':'world','hello':'world'},[1,2,3,4,5]),
      ('hello1',0,{'hellow':'worldw','hesllow':'worldw'},[1,2,3,4,5]),
      ('hello2',0,{'helloq':'worldq','heslloq':'worldq'},[1,2,3,4,5])]

sc=StructType([
    StructField('name',StringType(),True),
    StructField('num',IntegerType(),True),
    StructField('keyvalues',MapType(StringType(),StringType()),True),
    StructField('seq',ArrayType(IntegerType()),True)
])

df=spark.createDataFrame(data=data,schema=sc)

df.printSchema()


df.show(trunscate=False)
