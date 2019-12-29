# read data sets
# every 4 positions is a data set
# postiion 0 in data set is instruction
#    1 = add
#    2 = multiply
#    99 = end program
# position 1 and 2 are pointers to data
# position 3 is a pointer to where to store result
import csv
for noun in range(100):
    for verb in range(100):
        with open('data.csv') as csv_file:
            data = list(csv.reader(csv_file, delimiter=','))
        data[0][1]=str(noun)
        data[0][2]=str(verb)
        i = 0
        while int(data[0][i]) != 99:
            x = int(data[0][i])
            if x==1:
                data[0][int(data[0][i+3])] = str(int(data[0][int(data[0][i+1])]) + int(data[0][int(data[0][i+2])]))
            else:
                data[0][int(data[0][i+3])] = str(int(data[0][int(data[0][i+1])]) * int(data[0][int(data[0][i+2])]))
            i+=4
        if data[0][0] == '19690720':
            print 100*noun + verb        
    
