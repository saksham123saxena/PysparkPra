import Common as s
'''
will create the dataframe from table view
'''
li=[("sohan",1),("rohan",2)]
df=s.spark.createDataFrame(li,schema=['name ',' age'])
df.printSchema()
df.createOrReplaceTempView('table1')
s.spark.sql("select * from table1").show()

dff=s.spark.table("table1")
dff.printSchema()
dff.show()


