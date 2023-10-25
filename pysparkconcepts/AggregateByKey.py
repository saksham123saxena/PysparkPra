from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("UseOfAggregateByKey").getOrCreate()

##function logic for getting the maximum seq
def seq_op(acc,ele):
    if(acc>ele[1]):
        return acc
    else:
        return ele[1]

def comp_op(acc1,acc2):
    if(acc1>acc2):
        return acc1
    else:
        return acc2


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

## creating the collection for applying the transformation
rdd1=rdd.map(lambda x: (x[0],(x[1],x[2])))

##printing the rdd result
for x in rdd1.collect():
    print(x)

zero_val=0

##now, using aggregatebykey transformation

aggr_rdd=rdd1.aggregateByKey(zero_val,seq_op,comp_op)

##printing the result of final rdd
for x in aggr_rdd.collect():
    print(x)

