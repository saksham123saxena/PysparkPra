from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import date, datetime
import datetime

spark=SparkSession.builder.master("local").appName("BatchJobPipelines")\
    .config("spark.jars", "/Users/sakshamsaxena/Downloads/postgresql-42.7.0.jar").getOrCreate()

url = "jdbc:postgresql://10.60.0.23:5440/kooapp"
batch_size = 500
offset = 0

def generate_unique_filename():
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"output_{timestamp_str}.parquet"

partition=date.today()
try:
    properties={
        "user": "de_read_only",
        "password": "VE4xUSSdlCb4TPp",
        "driver": "org.postgresql.Driver"
    }
    table_name = "reported_koos"
    df = spark.read.jdbc(url, table_name, properties=properties)
    df.createOrReplaceTempView("reportedkoo")
    just_count=0
    while offset<=4000:
        sql_df = f"SELECT * FROM reportedkoo where id >={offset} and id<={batch_size}"
        result_df = spark.sql(sql_df)
        print(result_df.count())
        result_df.rdd.repartition(1)
        parquet_filename = generate_unique_filename()
        result_df.write.parquet(f"/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/batchjob/{partition}/{parquet_filename}",mode="overwrite")
        offset=batch_size
        batch_size=batch_size+batch_size
        print(str(batch_size)+"   "+str(offset))

except Exception as err:
    print("erorr of except block "+str(err))

