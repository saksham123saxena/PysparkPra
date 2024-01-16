from pyspark.sql import SparkSession
from datetime import date, datetime
import datetime
import subprocess

spark=SparkSession.builder.master("local").appName("BatchJobPipelines")\
    .config("spark.jars", "/Users/sakshamsaxena/Downloads/postgresql-42.7.0.jar").getOrCreate()

url = "jdbc:postgresql://10.60.0.23:5440/kooapp"
batch_size = 500
offset = 1072699

def curl_request(url):

    # Define the command to execute using curl
    command = ['curl', '-s', '-o', '-', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Return the stdout of the curl command
    return result.stdout

# Make a curl request to https://www.google.com/
response = curl_request('')

# Make a curl request to https://www.google.com/
print(response)



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
    table_name = "users"
    df = spark.read.jdbc(url, table_name, properties=properties)
    df.createOrReplaceTempView("users")
    just_count=0
    while offset<=1082699:
        sql_df = f"SELECT * FROM users where id >={offset} and id<={batch_size+offset}"
        result_df = spark.sql(sql_df)
        print(result_df.count())
        result_df=result_df.select("id","handle","encrypted_phone");
        result_df.rdd.repartition(1)
        result_df.show(10)
        parquet_filename = generate_unique_filename()
        result_df.write.parquet(f"/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/batchjob/{partition}/*.",mode="overwrite")
        offset=batch_size
        batch_size=batch_size+batch_size
        print(str(batch_size)+"   "+str(offset))

except Exception as err:
    print("erorr of except block "+str(err))

