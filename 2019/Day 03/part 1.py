import csv
import numpy

width = 100000
wires = [width][width]
centre = width/2

with open('data.csv') as csv_file:
    data = list(csv.reader(csv_file, delimiter=','))

for i in data:
    print (data[0,i])
    
