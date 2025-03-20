#import functions
from pyspark.sql import SparkSession


#membuat app spark
spark = SparkSession.builder \
.appName("WriteToPostgres") \
.config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
.getOrCreate()

#membaca data
data = spark.read.csv('/opt/airflow/data/Extract.csv', header=True, inferSchema=True)
#menghapus data yang missing values
data1 = data.na.drop()
#menghapus data yang duplikat
data2 = data1.dropDuplicates()
#ekspor data ke Transform.csv
data2.write.csv('/opt/airflow/data/Transform.csv', header=True, mode = "overwrite")