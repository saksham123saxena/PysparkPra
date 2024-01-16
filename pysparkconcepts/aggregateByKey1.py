from pyspark import SparkSession
spark=SparkSession\
    .builder\
    .master("local")\
    .appName("ExampleOfAggregateByKey")\
    .getOrCreate()

def seq_op(acc,ele):
    if(acc[1]>ele[1]):
        return acc
    else:
        return ele
def seq_op1(acc,ele):
    return (acc[0]+ele[1],acc[1]+1)

def comp_op(acc1,acc2):
    if(acc1[1]>acc2[1]):
        return acc1
    else:
        return acc2

def comp_op1(acc1,acc2):
    return (acc1[0]+acc2[0],acc1[1]+acc2[1])

rdd=spark.sparkContext.parallelize([
    (2,"joseph",200),
    (2,"jimmy",250),
    (2,"tina",130),
    (4,"jimmy",50),
    (4,"tina",300),
    (4,"joseph",150),
    (4,"ram",200),
    (2,"tina",200),
    (7,"joseph",300),
    (7,"jimmy",80)
],2)

zero_agg=(0,0)
rdd1=rdd.map(lambda x:(x[0],(x[1],x[2])))

aggr_rdd=rdd1.aggregateByKey(zero_agg,seq_op,comp_op)

for ele in aggr_rdd.collect():
    print(ele)


print("printing the sum and count !!!!!!!!!")

aggr_rdd1=rdd1.aggregateByKey(zero_agg,seq_op1,comp_op1)

for ele in aggr_rdd1.collect():
    print(ele)


