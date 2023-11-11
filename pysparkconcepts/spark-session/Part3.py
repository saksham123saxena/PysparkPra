import Common as s
'''
tempView: two type of temp view
1-> normal [way: createTempView or createOrReplaceTempView]
2-> global [way: createGlobalTempView or createOrReplaceGlobalTempView]
'''

li=[("sohan",1),("rohan",2)]
li1=[("swohan",1),("rowhan",2)]
df=s.spark.createDataFrame(li,schema=['name ',' age'])
df1=s.spark.createDataFrame(li1,schema=['name ',' age'])
df.printSchema()
df.createOrReplaceTempView('table1')
df1.createOrReplaceTempView("table2")
s.spark.sql("select * from table1").show()
s.spark.sql("select * from table2").show()
 ## -> check : global_temp is not working with global temp view table
