from pyspark import SparkSession
sc=SparkSession.builder.master("local").appName("WebVisualization").getOrCreate()


rdd=sc.sparkContext.textFile("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/wordcounts.text")
wordCount=rdd.flatMap(lambda x: x.split(","))
for ele in wordCount.top(10):
    print(ele)

worlcollection=wordCount.map(lambda x:(x,1))

print("-----------------")
for ele in worlcollection.top(10):
    print(ele)

wordSum=worlcollection.reduceByKey(lambda x,y:x+y)

print("-----------------")
for ele in wordSum.top(10):
    print(ele)


finalAns=wordSum.takeOrdered(3,lambda k:-float(k[1]))


print("final answer : "+str(finalAns))
print(wordSum.toDebugString())
#
for ele in wordSum.toDebugString().split("\n") : print(ele)


'''
b'(1) PythonRDD[10] at RDD at PythonRDD.scala:53 []\n | 
MapPartitionsRDD[7] at mapPartitions at PythonRDD.scala:145 []\n |  
ShuffledRDD[6] at partitionBy at NativeMethodAccessorImpl.java:0 []\n 
+-(1) PairwiseRDD[5] at reduceByKey at /Users/sakshamsaxena/PycharmProjects/TutPyspark/pysparkconcepts/WebVis.py:16 []\n    | 
PythonRDD[4] at reduceByKey at /Users/sakshamsaxena/PycharmProjects/TutPyspark/pysparkconcepts/WebVis.py:16 []\n    |  
/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/wordcounts.text MapPartitionsRDD[1] at textFile at NativeMethodAccessorImpl.java:0 []\n    |  
/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/wordcounts.text HadoopRDD[0] at textFile at NativeMethodAccessorImpl.java:0 []'

'''
