from pyspark.sql import SparkSession
sc=SparkSession.builder.master("local").appName("Broad_Casting_of_Variable").getOrCreate()

day={"sun":"Sunday","mon":"Monday","tus":"tuesday"}
print(day)
days=sc.sparkContext.broadcast(day)
print("type of days variable "+str(type(days))) ## type of days variable <class 'pyspark.broadcast.Broadcast'>
print(days.value)

print(days.value["sun"])

def converting(dic_key):
    return days.value[dic_key]

data=[("Saksham","Saxena","USA","sun"),
      ("Msnj","sdk","USA","mon"),
      ("sndjns","ww","USA","tus")]

rdd=sc.sparkContext.parallelize(data)
print("------- way of printing input data ---------")
inpu=rdd.map(lambda x:(x[0],x[1],x[2],x[3])).collect()

print(inpu)

outp=rdd.map(lambda x:(x[0],x[1],x[2],converting(x[3]))).collect()
print("------- way of printing output data ---------")
print(outp)

