from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark=SparkSession.builder.master("local").appName("ColumnObject").getOrCreate()

data=[Row(name="hello",type=1),Row(name="hello",type=2),Row(name="hello",type=3),
      Row(name="hello",type=None)]
rdd=spark.sparkContext.parallelize(data)
print("printing the element of rdd!!")
for ele in rdd.collect():
    print(ele)

sc=StructType([
    StructField("name",StringType(),True),
    StructField("type",IntegerType(),True)
])

df=spark.createDataFrame(data=rdd,schema=sc);
df.printSchema()
df.show()
print("performing the column operation!!")

# df.select(df.name).show()
# df.select(df["name"]).show()
# df.select(col("name")).show()
#
# df.select(col("type").alias("alias_type")).show()
#
# df.orderBy(df.type.desc()).show() # way of using order by increasing or decreasing

df.select(df.name).distinct().show()

df.where(df.type.between(1,3)).show()
df.where(df.name.contains("hello")).show()
df.where(df.type.contains(2)).show()

# df.where(df.name.startsWith('h')).show() # will check again this startsWith function

df.where(df.type.isin(1,2)).show()

# way of using casting

# df1=df.select(df.type.cast("string"))
# df1.printSchema()
# df1.show()

df.select(df.type==1).show()
df.select(df.type==1,df.type.eqNullSafe(1).alias("eqNullSafe"),df.type.isNull().alias("isnull")).show()
df.select((df.name.substr(1,3)=='hel').alias("containHel")).show()

dff=spark.createDataFrame([Row(r=Row(a1=1,a2="b")),Row(r=Row(a1=2,a2="bb"))])
dff.printSchema()
dff.show()

dff.select(dff.r.a1).show()
dff.select(dff.r.getField('a1')).show()

dff1=spark.createDataFrame([([1,2],{"key":"value"})],["list","dict"])
dff1.printSchema()
dff1.show()
print("priting of array and dict part!!")
dff1.select((dff1.list[1]).alias("list"),(dff1.dict['key']).alias('dictin')).show()
dff1.select(dff1.list.getItem(1).alias("list"),dff1.dict.getItem('key').alias('dictin')).show()

# Way of using when

df.select(df.type,
          when(df.type == 1,"One")
          .when(df.type == 2,"Two")
          .when(df.type == 3,"Three")).show()
