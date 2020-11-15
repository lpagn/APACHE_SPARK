print("gen.py")

i = 0

f = open('test_file.csv', 'w')

A = 50000000
B = 50000000

while i < A:
	f.write("a\n")
	#f.write("a\n")
	i=i+1

i = 0

while i < B:
	f.write("b\n")
	#f.write("b\n")
	i=i+1

print("end")
