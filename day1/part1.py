import pandas as pd
import time
import csv

#path = 'input.csv'

def day_1_part_1('input.csv'):
    df = pd.read_csv(path, sep = ',', names = ['numbers'])
    values = set(df['numbers'])
    for i in values:
        if (2020-i) in values:
                return(i*(2020-i))

start = time.time()
result = day_1_part_1(path)            
runtime = time.time() - start
print('Result:',result)
print('Runtime:', runtime)
