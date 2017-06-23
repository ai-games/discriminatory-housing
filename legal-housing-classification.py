# June 9, 2017
# Script will allow user to label posts as discriminatory or not.
# Then it will save to a new file.

import json

print('type quit to quit\n\n')

labeledData = []
with open('./listings3.json') as f:
    data = json.load(f)
    label = ''
    
    for line in data:
        if label == 'quit':
            line['discriminatory'] = ''
            labeledData.append(line)
        elif 'discriminatory' in line.keys() and (line['discriminatory'] == True or line['discriminatory'] == False):
            continue
        else:
            print('\n\n\n\n\n')
            print(line['description'])
            label = input('\n\nis discriminatory (y/n):  ')

            if label == 'quit':
                line['discriminatory'] = ''
                labeledData.append(line)
            else:
                line['discriminatory'] = True if label == 'y' else False
                labeledData.append(line)
    
        
    
fout = open('./listing3-labeled.json', 'w')
fout.write('[')
count = 0
maxLen = len(labeledData)
for i in labeledData:
    fout.write(json.dumps(i))
    count += 1
    if (count < maxLen):
        fout.write(',\n')
fout.write(']')

fout.close()
