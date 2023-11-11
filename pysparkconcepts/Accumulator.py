from pyspark.sql import SparkSession
sc=SparkSession.builder.master("local").appName("Broad_Casting_of_Variable").getOrCreate()



rdd=sc.sparkContext.parallelize([1,2,3])
print(rdd)
def countingIteration(x):
    global counter1
    counter1.add(1)

counter1=sc.sparkContext.accumulator(0)  ## here, 0 is initial value of accumulator counter1
print(counter1)
print(type(counter1))
rdd.foreach(countingIteration)
print(counter1)



