from pyspark.sql import SparkSession #REQUIRED PACKAGES ARE IMPORTED
import pandas as pd
import subprocess
spark=SparkSession.builder.appName("groupbyagg").getOrCreate()
df=spark.read.csv("/user/kaggle/kaggle_data/toefl_uni_selection/original_data.csv",inferSchema=True,header=True) # DATASET IS READ FROM GIVEN DIRECTORY.
df.printSchema() #PRINTING THE SCHEMA
df.createOrReplaceTempView("df") #CREATING THE TABLE FOR APPLYING SQL QUERY.
df.show()# PRINTING WHOLE TABLE.
df3=spark.sql("SELECT * FROM df WHERE major IS NOT NULL AND toeflScore IS NOT NULL") # NULL VALUES OF ROWS FROM MAJOR AND TOEFLSCORE ARE REMOVED BY SQL QUERY.
df.createOrReplaceTempView("df3") #CREATING A TABLE.
df4=spark.sql("SELECT major,avg(toeflScore) FROM df3 group by major") #APPLYING SQL QUERY FOR GROUPBY ON COLUMNS MAJOR AND ALSO AVERAGE OF TOEFLSCORE FOR RESPECTIVE MAJORS.
df4.show(245) # PRINTING TABLE OF 245 ROWS AS IT 'S CAPACITY IS ONLY 245.

df4.write.mode("overwrite").csv('/user/sgangin/csv1_out', header = True, sep = '      ') # A FUNCTION FOR MULTIPLE PARTITIONS OF OUTPUT
data1 = []
data2 = []
[data1.append(data[0]) for data in df4.
       select('major').collect()]               #CONVERTING TABLE 2 COLUMNS INTO 2 LISTS AS A PREPROCESSING.
[data2.append(data[0]) for data in df4.
       select('avg(toeflScore)').collect()]

#print(data1)
#print(data2)

f = open("/home/sgangin/test.txt", "w") #AUTOMATICALLY A FILE IS CREATED IN OUR LOCAL HOST.
i = 0
f.write("Major"+","+"Average(ToeflScore)"+"\n");
for i in range(len(data1)):
    f.write(str(data1[i])+","+str(data2[i])+"\n")  #ADDING THE TABLE IN TEXTFORMAT TO A CREATED FILE IN LOCALHOST.

f.close()

subprocess.call("touch test.txt", shell = True)
#status = subprocess.call("hdfs dfs -rm -R /user/sgangin/out2", shell = True)
subprocess.call("hdfs dfs -mkdir -p /user/sgangin/out2", shell = True) # A DIRECTORY IS CREATED IN HDFS.
subprocess.call("hdfs dfs -put test.txt /user/sgangin/out2/output.txt", shell = True) # FROM LOCALHOST FILE MATTER IS SENT TO CREATED DIRECTORY IN HDFS.
dcsv = pd.read_csv("/home/sgangin/test.txt")   #A TEXT FILE IS READ FROM LOCALHOST 
dcsv.to_csv("/home/sgangin/test.csv", index = None) #IT IS CONVERTED TO CSV FILE BY THIS FUNCTION.
subprocess.call("hdfs dfs -put /home/sgangin/test.csv /user/sgangin/out2/output.csv", shell = True) # FROM LOCALHOST FILE MATTER IS SENT TO CREATED DIRECTORY IN HDFS.
