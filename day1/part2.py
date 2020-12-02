import pandas as pd
import time
import csv

path = 'input.csv'

def day_1_part_2(path):
    df = pd.read_csv(path, sep = ',', names = ['numbers'])
    values = set(df['numbers'])
    for i in values:
        for j in values:
            if (2020-(i+j)) in values:
                return(i*j*(2020-(i+j)))

start = time.time()
result = day_1_part_2(path)
runtime = time.time() - start

print('Result:',result)
print('Runtime:', runtime)     