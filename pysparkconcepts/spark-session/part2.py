import Common as s
from pyspark.sql import Row
import pandas as pd
'''
# creating DF from list
li=[('Rohan',1),('Sohan',2)]
df=s.spark.createDataFrame(li)  # here, we are not giving schema
df.show()
df.printSchema()
schema=['Name','RollNo']

df1=s.spark.createDataFrame(li,schema=schema) # here, we are giving schema with col names
df1.show()
df1.printSchema()

df2=s.spark.createDataFrame(li,schema=('Name String,Roll Int'))
df2.show()
df2.printSchema()

'''

'''
# now, creating DF from Dictionary

dic=[{"name":"rohan","age":12},{"name":"sohan","age":13}]
df=s.spark.createDataFrame(data=dic)
df.printSchema()
df.show()

'''

'''
# now, creating DF from RDD
li=[('Rohan',1),('Sohan',2)]
rdd=s.spark.sparkContext.parallelize(li)
print(type(rdd))
for ele in rdd.collect():
    print(ele)

df=s.spark.createDataFrame(rdd,schema=('name String,age Int'))
df.printSchema()
df.show()

'''

'''
# now, will discuss ROW | will create the RDD via list of ROW
val=Row(name="rohan",age=23)
print(type(val))
print(val.name)
print(val.age)
ans='name' in val
print(ans)

rdd=s.spark.sparkContext.parallelize([Row(name='rohan',age=12),Row(name='sohan',age=12)])
for ele in rdd.collect():
    print(ele)
df=s.spark.createDataFrame(rdd)
df.show()
df.printSchema()
'''

# now, creating DF from pandas
# [pandas: is nothing but two structure with name row and column. Consequently data is available in row and columns format]

li=[['tom',1],['jerry',2],['spike',3]]
pd_df=pd.DataFrame(data=li,columns=['Name','Roll_No'])
print(type(pd_df))
print(pd_df)
dff=s.spark.createDataFrame(pd_df) # having issues, due to padas version
dff.printSchema()
