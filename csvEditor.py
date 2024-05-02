import csv
from random import *

with open('healthData.csv', 'w') as file:
    for i in csv.reader(file):
        if (random.randint(0, 1) == 0):
            data = [i, randint(2400, 3000), randint(83, 115), data[2] * 100, randint(1,10), 'M']
        else:
            data = [i, randint(2000, 2500), randint(66, 81), data[2] * 100, randint(1,10), 'F']
        file.write(data)
    reader = csv.reader(file)
    for row in reader:
        print(row)
