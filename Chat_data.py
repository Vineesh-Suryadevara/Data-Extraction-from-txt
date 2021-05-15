# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:44:02 2021

@author: Vineesh
"""
import pandas as pd
from datetime import datetime
cols = ['collection_number','conversation_number','start_time','started_by','end_time','ended_by']

with open(r'D:/Geeky/DataSciecne/DataSets/chat_data.txt','r') as chatFile:
    content = chatFile.read()
    chatFile.close()
    
conv = content.split('**********************************************************')
while ('' in conv):
    conv.remove('')

convLines = []
for i in range(len(conv)):
        convLines.append(conv[i].split('\n'))
        j = 0
        while ('' in convLines[i]):
            convLines[i].remove('')
        while True:
            convLines[i][j] = convLines[i][j].strip()
            if convLines[i][j].startswith('x'):
                convLines[i][j-1] += '\n'+convLines[i][j]
                del(convLines[i][j])
            else:
                j += 1
            if j == len(convLines[i]):
                break

data = []
for cl in convLines:
    temprcd = []
    temp = cl[0].split('|')
    temprcd.append(temp[0].split(':')[1])
    temprcd.append(temp[1].split(':')[1])
    temp = cl[1].split(' ')
    startdt = datetime.strptime(temp[1][1:] +' '+ temp[2][:-7], '%Y-%m-%d %H:%M:%S')
    temprcd.append(startdt)
    temprcd.append(temp[0])
    temp = cl[-1].split(' ')
    enddt = datetime.strptime(temp[1][1:] +' '+ temp[2][:-7], '%Y-%m-%d %H:%M:%S')
    temprcd.append(enddt)  
    temprcd.append(temp[0])
    data.append(temprcd)

chatDF = pd.DataFrame(data = data, columns = cols)
print(chatDF.head())
