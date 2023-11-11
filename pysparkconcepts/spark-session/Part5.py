import Common as s

'''
conf : it is use for provide runtime configurations, shuffle parameters ,application configurations
using --conf or spark.conf
'''

print(s.spark.conf.get("spark.sql.shuffle.partitions")) # By Default, it is 200
s.spark.conf.set("spark.sql.shuffle.partitions",300) #set the value of spark.sql.shuffle.partitions value from 200 default to 300
print(s.spark.conf.get("spark.sql.shuffle.partitions"))
