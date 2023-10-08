from pyspark.sql import SparkSession
sc=SparkSession.builder.master("local").appName("PysparkTut").getOrCreate()
rd=sc.sparkContext.parallelize([1,2,3])
print(rd)
for r in rd.collect():
    print(r)

empData = [(7389, "SMITH", "CLEARK", 9902, "2010-12-17", 8000.00, 20),
            (7499, "ALLEN", "SALESMAN", 9698, "2011-02-20", 9000.00, 30)]

empRDD = sc.sparkContext.parallelize(empData)

for row in empRDD.collect():
      print(row)
