'''
reading CSV file
- by default spark read function is using all dataframe columns as string datatypes
- we can provide the schema information like that : schema='SNo int,Intro string,Name string,Roll int,Marks float,PreM float,PostM float,Loc string,DesLoc string,floatingVal float'
- we can also auto detect schema by  inferSchema=True
'''

import Common as s



# print(help(s.spark.read.csv)) # use to print all information about spark.read.csv file
# df=s.spark.read.load("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/demo.csv",
#                      format='csv',
#                      header=True,schema='SNo int,Intro string,Name string,Roll int,Marks float,PreM float,PostM float,Loc string,DesLoc string,floatingVal float')
# df.printSchema()
# df.show(10)
# df.show(10,truncate=False)


df=s.spark.read.load("/Users/sakshamsaxena/PycharmProjects/TutPyspark/sourcedata/demo.csv",
                     format='csv',
                     header=True, inferSchema=True)
df.printSchema()
df.show(10)
df.show(10,truncate=False)
