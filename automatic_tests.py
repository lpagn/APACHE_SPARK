"""SimpleApp.py"""
from pyspark.sql import SparkSession
import time
import pandas as pd

def spark():
    print('spark')
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
    return elapsed_time

def manual():
    print('manual')
    start_time = time.time()

    file1 = open('test_file.csv', 'r')
    Lines = file1.readlines()

    count = 0
    a=0
    b=0
    # Strips the newline character
    for line in Lines:
        #print("Line{}: {}".format(count, line.strip()))
        count +=1
        if line.find('a')!=-1:
            #print(line)
            a+=1

        if line.find('b')!=-1:
            #print(line)
            b+=1

    elapsed_time = time.time() - start_time

    print("Lines with a: %i, lines with b: %i" % (a,b))

    print("Total time to perform calculation %f" % (elapsed_time))

    file1.close()
    return elapsed_time
def gen(lines):
    print('gen')
    i = 0

    f = open('test_file.csv', 'w')

    A = lines/2
    B = lines/2

    while i < A:
    	f.write("a\n")
    	#f.write("a\n")
    	i=i+1

    i = 0

    while i < B:
    	f.write("b\n")
    	#f.write("b\n")
    	i=i+1

#index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index = [0,1,2,3,4,5,6]

columns = ['Spark','Manual','Lines']
df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0) # with 0s rather than NaNs

print('automatic tests')
lines = 10000000
i=0
while lines <= 70000000:
    print(lines)
    gen(lines)
    s = spark()
    m = manual()
    df_.at[i] = (s,m,lines)
    lines += 10000000
    i+=1

print(df_)

df_.plot(x ='Lines', y='Spark', kind = 'scatter')
df_.plot(x ='Lines', y='Manual', kind = 'scatter')

import matplotlib.pyplot as plt
fig1 = plt.figure()

ax1 = fig1.add_subplot(111)

ax1.plot(df_['Manual'])
ax1.plot(df_['Spark'])

plt.savefig('compare.png')
