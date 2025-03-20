#import functions
import requests
import os
import pymongo
from pymongo import MongoClient
from pyspark.sql import SparkSession
import pandas as pd

#membuat app spark
spark = SparkSession.builder \
.appName("WriteToPostgres") \
.config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
.getOrCreate()

#membaca data

data = spark.read.csv('/opt/airflow/data/Transform.csv', header=True, inferSchema=True)
pandas_data = data.toPandas()
client = MongoClient("mongodb+srv://adhirizqi1:perikitiw1603@cluster0.ft0r8.mongodb.net/")
document_list = pandas_data.to_dict(orient='records')
client['M3']['data'].insert_many(document_list)