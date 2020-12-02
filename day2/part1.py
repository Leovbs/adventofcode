import pandas as pd
import time
import csv

path = 'input.csv'

def make_minmax(data):
    minmax= []
    for i in data:
        aux = i.split('-')
        minmax.append([int(aux[0]),int(aux[1])])
    return(minmax)

def replace_to_blank(string):
    return(string.replace(':',''))

def make_letter_list(data):
    letter = list(map(replace_to_blank,data))
    return(letter)

def day_2_part_1(path):
    counter = 0
    df = pd.read_csv(path, sep = ' ', names = ['n','l','p'])
    
    minmax_list = make_minmax(df['n'])
    letter_list = make_letter_list(df['l'])
    passwords_list = list(df['p'])
    
    all_lists = [minmax_list,letter_list,passwords_list]
    
    for i in range (0, len(all_lists[0])):
        if ((all_lists[2][i].count(all_lists[1][i]) >= all_lists[0][i][0]) and (all_lists[2][i].count(all_lists[1][i]) <= all_lists[0][i][1])):
            counter += 1
    return(counter)     


start = time.time()
result = day_2_part_1(path)            
runtime = time.time() - start
print('Result:',result)
print('Runtime:', runtime)