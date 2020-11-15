import time

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
