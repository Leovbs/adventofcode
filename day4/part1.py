import time

f = open('input4.txt')

l = f.readlines()
for i in range(0,len(l)):
    l[i] = l[i].replace('\n','')

l.append('') #to fix the loop that is comming

final = []
aux = []
for line in l:
    if line == '':
        final.append(aux)
        aux = []
    else:
        aux.append(line)
        
for i in range(0, len(final)):
    aux_2 = final[i][0].split(' ')
    if len(final[i]) > 1:
        for j in range(1, len(final[i])):
            string = final[i][j].split(' ')
            for k in string:
                aux_2.append(k)
    final[i] = aux_2
    
checklist = ['byr','iyr', 'eyr','hgt','hcl','ecl','pid']

valid_passport = []
for passport in range(0,len(final)):
    checks = [0]*7
    for field in range (0, len(final[passport])):
        aux = final[passport][field].split(':')
        if aux[0] in checklist:
            checks[checklist.index(aux[0])] = 1
    if sum(checks) == 7:
        valid_passport.append(final[passport])
            
print(len(valid_passport))