#import functions
from pyspark.sql import SparkSession

#membuat app spark
spark = SparkSession.builder \
.appName("WriteToPostgres") \
.config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
.getOrCreate()

#membaca data
data = spark.read.csv('/opt/airflow/data/BankChurner.csv', header=True)

#ekspor data ke Extract.csv
data.write.csv('/opt/airflow/data/Extract.csv', header=True, mode = "overwrite")