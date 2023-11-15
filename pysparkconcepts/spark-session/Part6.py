'''
 # - below code for creating UDF via register method way
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)


def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr



# Converting function to UDF
convertUDF = udf(lambda z: convertCase(z),StringType())


df.select(col("Seqno"), \
    convertUDF(col("Name")).alias("Name") ) \
   .show(truncate=False)

df.select(df.Name,convertUDF(df.Name).alias("New-Name")).show()



'''

# ====== creating UDF via @udf way
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)

@udf(returnType=StringType())
def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr



# Converting function to UDF
# convertUDF = udf(lambda z: convertCase(z),StringType())


df.select(col("Seqno"), \
    convertCase(col("Name")).alias("Name") ) \
   .show(truncate=False)

df.select(df.Name,convertCase(df.Name).alias("New-Name")).show()


'''

#== now, using UDF via sql expression


'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr



# Converting function to UDF
spark.udf.register("convertUDF", convertCase,StringType())

spark.sql("""
select convertUDF("i am pyspark developer") as newCol
""").show()

'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType,IntegerType
import Common as c
# using lambda function
func= udf(lambda x:len(x),IntegerType())
c.spark.udf.register("lengthCal",func) # way of register lambda function

c.spark.sql("""
select lengthCal("hello")
""").show()
