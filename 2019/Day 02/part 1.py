# read data sets
# every 4 positions is a data set
# postiion 0 in data set is instruction
#    1 = add
#    2 = multiply
#    99 = end program
# position 1 and 2 are pointers to data
# position 3 is a pointer to where to store result
import csv
with open('data.csv') as csv_file:
    data = list(csv.reader(csv_file, delimiter=','))
i = 0
data[0][1]='12'
data[0][2]='2'
while int(data[0][i]) != 99:
    print i
    x = int(data[0][i])
    print x
    if x==1:
        data[0][int(data[0][i+3])] = str(int(data[0][int(data[0][i+1])]) + int(data[0][int(data[0][i+2])]))
        print 'add'
    else:
        data[0][int(data[0][i+3])] = str(int(data[0][int(data[0][i+1])]) * int(data[0][int(data[0][i+2])]))
        print 'multiply'
    i+=4
print data[0][0]

        
    
