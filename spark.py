"""SimpleApp.py"""
from pyspark.sql import SparkSession
import time

print("Apache Spark Demo")

logFile = "/Users/luciopagni/Desktop/APACHE_SPARK/test_file.csv"
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

start_time = time.time()

logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

elapsed_time = time.time() - start_time

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

print("Total time to perform calculation %f" % (elapsed_time))

spark.stop()
